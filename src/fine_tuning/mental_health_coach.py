import json, re
import pandas as pd
from pathlib import Path
import api
from langdetect import detect
from unidecode import unidecode
from logger import Logger
from datasets import load_dataset
from fine_tuning.dataset_validator import validate_messages


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


data = load_data()

# generate messages
if not Path(FILE_PATH).is_file():
    data.apply(format_messages, axis=1)

# validate messages
validate_messages(FILE_PATH)
