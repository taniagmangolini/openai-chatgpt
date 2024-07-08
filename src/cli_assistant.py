import api
import os
import math
import click
from util.logger import Logger
from messages.few_shots import cli_task


logger = Logger().get_logger()


while True:
    messages = cli_task.copy()

    # read the input
    request = input(
      click.style(
        "Input: ", 
        fg="green"
      )
    )

    if request == 'exit':
        exit()
    
    # add input to the messages
    messages.append(
        {
            "role": "user",
            "content": f"{request}"
        }
    )
    
    # ask the model to generate de command to perform the desired cli task
    command_output = api.create_chat_completion("gpt-3.5-turbo", messages, temperature=0)

    # Show the command returned by the model to be executed on the command line interface
    click.echo(
      click.style(
        "Output: ", fg="yellow"
      ) + command_output
    )
    click.echo()


    # ask the user if they want to execute the command
    click.echo(
      click.style(
        "Execute? (y/n): ", 
        fg="yellow"
      ), 
      nl=False
    )

    # Read the user input
    choice = input()

    if choice not in ["y", "n"]:
        click.echo(
            click.style(
            "Invalid choice. Please enter 'y' or 'n'.", 
            fg="red"
            )
        )
    
    # If yes, execute the command
    if choice == "y":
      r = os.system(command_output)
      if r != 0:
        click.echo(
          click.style(
            "Error executing command.", 
            fg="red"
          )
        )
    else:
        continue