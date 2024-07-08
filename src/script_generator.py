import api
from util.logger import Logger
from messages.few_shots import (
    get_messages_for_prompt_and_behaviour,
    PROMPT_FOR_PYTHON_DOCKERFILE, 
    PROMPT_FOR_MYSQL_KUBERNETS_DEPLOYMENT
)


logger = Logger().get_logger()


def generate_script(model, prompt):
    """Task to generate a script for a specific task."""
    result = api.create_chat_completion(
        model, 
        prompt, 
    )
    return result


if __name__ == "__main__":
    for prompt in [
        PROMPT_FOR_PYTHON_DOCKERFILE, 
        PROMPT_FOR_MYSQL_KUBERNETS_DEPLOYMENT
    ]: 
        behaviour = "You are a smart assistant who writes "\
        "configuration scripts."
        messages = get_messages_for_prompt_and_behaviour(prompt, behaviour)
        script = generate_script("gpt-3.5-turbo", messages)
        logger.info(f"Script: {script}")
