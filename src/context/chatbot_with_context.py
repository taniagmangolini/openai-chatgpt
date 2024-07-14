import api
import api
import click
from logger import Logger


logger = Logger().get_logger()


history = [{"role": "system", "content": "You are helpful assistant."}]

model = "gpt-3.5-turbo"


while True:

    # read the user input
    request = input(click.style("Input: (type 'exit' to quit): ", fg="green"))

    if request.lower() in ["exit", "quit"]:
        break

    # Add the message to the history
    history.append({"role": "user", "content": f"{request}"})

    # send the history to the API
    content = api.create_chat_completion(
        model=model,
        messages=history,
    )

    # add the the response to the history
    history.append({"role": "assistant", "content": f"{content}"})

    # Print the command in a nice way
    click.echo(click.style("Output: ", fg="yellow") + content)

    click.echo()
