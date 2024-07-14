import api
import click
from logger import Logger


logger = Logger().get_logger()


model = "gpt-3.5-turbo"

base_messages = [{"role": "system", "content": "You are helpful assistant."}]

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
        model=model,
        messages=messages,
    )

    # Print the command in a nice way
    click.echo(click.style("Output: ", fg="yellow") + content)

    click.echo()
