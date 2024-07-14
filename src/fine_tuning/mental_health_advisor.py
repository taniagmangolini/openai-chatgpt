import json, re
import click
import pandas as pd
from pathlib import Path
import api
from langdetect import detect
from unidecode import unidecode
from logger import Logger
from datasets import load_dataset
from fine_tuning.dataset_validator import validate_messages
from fine_tuning.fine_tuning_model_creator import (
    upload_tuning_file,
    upload_tuning_job,
    check_tuning_status,
)


logger = Logger().get_logger()


FILE_PATH = "fine_tuning/data/mental_health_data.jsonl"


def load_data():
    ds = load_dataset("Amod/mental_health_counseling_conversations", split="train")
    df = pd.DataFrame(ds).assign(
        formatted_context=lambda x: x["Context"].apply(lambda col: clean_text(col)),
        formatted_response=lambda x: x["Response"].apply(lambda col: clean_text(col)),
    )
    return df


def clean_text(text):
    # Replace common Unicode characters with ASCII equivalents
    text = unidecode(text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Correct spacing around punctuation
    text = re.sub(r"\s*([,.!?])\s*", r"\1 ", text)

    # Trim leading and trailing whitespace
    text = text.strip()

    # Correct space after punctuation if missing
    text = re.sub(r"([:,.!?])([^\s])", r"\1 \2", text)
    return text


def get_system_content():
    return "You are MendMind, an AI Mental Health Coach. \
    Your purpose is to support the user through their mental \
    health journey with empathy, understanding, and insights \
    into managing emotional and psychological challenges. \
    While you can provide general advice and emotional \
    support, you are not equipped to handle personal contact, \
    schedule appointments, or share any specific location \
    details. Your only role is to help the user with coping \
    strategies, provide information on mental health topics, \
    and guide them towards professional resources if needed. \
    You can engage in a regular conversation with the user, \
    but your primary focus is what you can do best: \
    supporting the user with confidentiality and care in \
    the path to well-being."


def get_message(role, content):
    return {"role": role, "content": content}


def save_messages(messages, filepath):
    with open(filepath, "a") as file:
        file.write(json.dumps(messages) + "\n")


def format_messages(row):
    try:
        context = row["formatted_context"]
        response = row["formatted_response"]
        print(type(row), row)
        # check context is not empty and the if response is longer than 10 words
        if len(context) > 0 and len(response.split()) > 10:
            # Check language
            if detect(context) == "en" and detect(response) == "en":
                system = get_message("system", get_system_content())
                user = get_message("user", context)
                assistant = get_message("assistant", response)
                messages = {"messages": [system, user, assistant]}
                save_messages(messages, FILE_PATH)
    except Exception as e:
        logger.info(f"Error: {e}\n Context: {context}\n Response: {response}")


if not Path(FILE_PATH).is_file():

    log.info("Loading data ...")
    data = load_data()

    # generate messages
    if not Path(FILE_PATH).is_file():
        data.apply(format_messages, axis=1)

    # validate messages
    validate_messages(FILE_PATH)


# tuning a model if it not exists
model = None
with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        if key == "FINE_TUNED_MODEL_HEALTH_COACH":
            model = value
            break

if not model:
    file_id = upload_tuning_file(FILE_PATH)
    fine_tune_job = upload_tuning_job(file_id)
    check_tuning_status(fine_tune_job)

# using the model
# This model is designed to provide a single response to a single input.
# It cannot handle a multiple turn conversation

logger.info(f"Using the model {model}")

base_messages = [
    {"role": "system", "content": get_system_content()},
    {
        "role": "assistant",
        "content": "My name is MendMind. "
        "I'm an AI Mental Health Coach. "
        "How can I help you today?",
    },
]

while True:
    messages = base_messages.copy()

    # read the user input
    request = input(click.style("Input: (type 'exit' to quit): ", fg="green"))

    if request.lower() in ["exit", "quit"]:
        break

    # add the user input to the messages
    messages.append({"role": "user", "content": f"{request}"})

    # send the messages to the API
    content = api.create_chat_completion(
        model, messages, temperature=0.7, frequency_penalty=0.5, presence_penalty=0.5
    )

    # Print the command in a nice way
    click.echo(click.style("Output: ", fg="yellow") + content)

    click.echo()
