import os
from flask import Flask, request
from openai import OpenAI
from weaviate_client import WeaviateClient


app = Flask(__name__)


with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value

openai_api_key = os.environ["API_KEY"]


schema = {
    "class": "Wikipedia",
    "description": "An article from Wikipedia",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        # How embeddings where created in the dataset
        "text2vec-openai": {
            "model": "ada",
            "modelVersion": "002",
            "type": "text",
            "vectorizeClassName": False,
        },
       "generative-openai": {
          "model": "gpt-3.5-turbo",  
          "temperatureProperty": 2,  
          "maxTokensProperty": 100, 
        },
    },
    "properties": [
        {
            "name": "title",
            "description": "The title of the article",
            "dataType": ["text"],
            "moduleConfig": {"text2vec-openai": {"skip": True}},
        },
        {
            "name": "content",
            "description": "The content of the article",
            "dataType": ["text"],
        },
    ],
}

openai_client = OpenAI(api_key=openai_api_key, organization=os.environ["ORG_ID"])

weaviate_client = WeaviateClient(app.logger, "Wikipedia", openai_api_key)
weaviate_client.weaviate_delete_data()
weaviate_client.weaviate_create_schema(schema)
weaviate_client.weaviate_import_data('data/wikipedia_data.csv')


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("q")
    prompt = """
            Summarize the following in a tweet in Portuguese:

            {title} - {content}
            """
    
    context = weaviate_client.weaviate_semantic_search(
        question, 
        prompt
    )

    return {
        "response": context
    }
