import click
import api
from logger import Logger
from utils import get_embedding, calc_cosine_similarity, generate_embeddings_for_dataset
import numpy as np


logger = Logger().get_logger()


def get_custom_model():
    with open(".env") as env:
        for line in env:
            if "FINE_TUNED_MODEL" in line:
                return line.strip().split("=")[1]


base_messages = [{"role": "system", "content": "You are a smart home assistant."}]


while True:
    messages = base_messages.copy()

    request = input(click.style("Input: (type 'exit' to quit): ", fg="green"))

    if request.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": f"{request}"})

    response = api.create_chat_completion(
        model=get_custom_model(),
        messages=messages,
        max_tokens=200,
        temperature=0,
    )

    click.echo(click.style("Output: ", fg="yellow") + response)

    click.echo()
