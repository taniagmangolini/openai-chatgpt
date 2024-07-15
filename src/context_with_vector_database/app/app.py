import os
from flask import Flask, request
from openai import OpenAI
from weaviate_client import WeaviateClient


app = Flask(__name__)


openai_api_key = os.environ["API_KEY"]
system_prompt = "You are a helpful assitant"
system_prompt = {"role": "system", "content": system_prompt} 

weaviate_limit = 10
interactions_limit = 10
weaviate_certainty = 0.5


with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value


openai_client = OpenAI(api_key=openai_api_key, organization=os.environ["ORG_ID"])

weaviate_client = WeaviateClient(app.logger, "ChatMessage", openai_api_key)


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("q")

    user_prompt = {"role": "user", "content": question}

    context = weaviate_client.weaviate_nearest_interactions(
        question, weaviate_certainty, weaviate_limit
    )

    latest_interactions = weaviate_client.weaviate_latest_interactions(
        interactions_limit
    )

    global_context = context["data"] + latest_interactions["data"]

    global_context = [dict(t) for t in {tuple(d.items()) for d in global_context}]

    messages = [system_prompt] + global_context + [user_prompt]

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=1.2,
    )

    content = response.choices[0].message.content.strip()

    assistant_prompt = {"role": "assistant", "content": content}

    data = [user_prompt, assistant_prompt]

    weaviate_client.weaviate_save_data(data)

    return {
        "response": assistant_prompt["content"],
        "global_context": global_context,
    }


schema = {
    "classes": [
        {
            "class": weaviate_client.class_name,
            "description": "A class to store chat messages",
            "properties": [
                {
                    "name": "content",
                    "description": "The content of the chat message",
                    "dataType": ["text"],
                },
                {
                    "name": "role",
                    "description": "The role of the message",
                    "dataType": ["string"],
                },
            ],
        }
    ]
}

weaviate_client.weaviate_delete_data()
weaviate_client.weaviate_create_schema(schema)
