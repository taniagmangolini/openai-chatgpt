import api
import json
import click
from logger import Logger
from utils import (
    get_embedding,
    calc_cosine_similarity,
    preprocess_text,
)


logger = Logger().get_logger()


context_window = 2
model = "gpt-3.5-turbo"
hitory_file_path = "context/data/context.txt"
full_history = []


global_context = [{"role": "system", "content": "You are helpful assistant."}]


def save_history_to_file(history):
    """
    Save the history of interactions to a file.
    """
    with open(hitory_file_path, "w") as f:
        f.write(json.dumps(history))


def load_history_from_file():
    """
    Load the history from a file.
    """
    with open(hitory_file_path, "r") as f:
        import json

        try:
            history = json.loads(f.read())
            return history
        except json.JSONDecodeError:
            return []


def sort_history(history, prompt, context_window):
    """
    Sort the history of interactions based
    on cosine similarity.
    Returns the top context_window segments.
    """
    sorted_history = []
    for segment in history:
        content = segment["content"]
        preprocessed_content = preprocess_text(content)
        preprocessed_prompt = preprocess_text(prompt)

        embedding_content = get_embedding(preprocessed_content)
        embedding_prompt = get_embedding(preprocessed_prompt)
        similarity = calc_cosine_similarity(embedding_content, embedding_prompt)
        sorted_history.append((segment, similarity))
    sorted_history = sorted(sorted_history, key=lambda x: x[1], reverse=True)
    sorted_history = [x[0] for x in sorted_history]
    return sorted_history[:context_window]


while True:

    request = input(click.style("Input: (type 'exit' to quit): ", fg="green"))

    if request.lower() in ["exit", "quit"]:
        break

    user_prompt = {"role": "user", "content": request}

    # Load the history from the file and append the new messages
    full_history = load_history_from_file()
    sorted_history = sort_history(full_history, request, context_window)
    sorted_history.append(user_prompt)
    messages = global_context + sorted_history
    # Send the messages to the API
    response = api.create_chat_completion(
        model=model,
        messages=messages,
        max_tokens=200,
        temperature=1,
    )

    # Debug: print the history
    click.echo(
        click.style("History: ", fg="blue") + str(json.dumps(messages, indent=4))
    )

    # Print the command in a nice way
    click.echo(click.style("Output: ", fg="yellow") + response)

    # Add the user prompt to the history
    full_history.append(user_prompt)
    # Add the response to the history
    full_history.append({"role": "assistant", "content": response})

    # Save the history to a file
    save_history_to_file(full_history)
