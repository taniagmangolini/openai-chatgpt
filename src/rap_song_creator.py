import api
from logger import Logger
from typing import Optional
from messages.few_shots import (
    get_messages_for_rap_knowledge_generation_task,
    get_messages_for_rap_lyrics_generation_task,
)


logger = Logger().get_logger()


def generate_rap_knowledge(model):
    """Chat completion task to get knowledge about rap."""
    logger.info(f"Generating knowledge about rap in order to feed the model that will generate the lyrics...")
    prompt = """Write a concise paragraph about the lyrical characteristics and themes of old-school rap."""
    messages = get_messages_for_rap_knowledge_generation_task(prompt)
    knowledge = api.create_chat_completion(model, messages, temperature=0.5, stop_token=["assistant:", "user:"])
    logger.info(f"Knowledge: {knowledge}")
    return knowledge


def generate_rap_lyrics(model):
    """Chat completion task to generate rap lyrics."""
    knowledge_about_rap = generate_rap_knowledge(model)
    messages = get_messages_for_rap_lyrics_generation_task(knowledge_about_rap)
    lyrics = api.create_chat_completion(model, messages, temperature=1, stop_token=["assistant:", "user:"])
    return lyrics


if __name__ == "__main__":   
    """General Knowledge Prompting which consists of generating knowledge about 
    the task by the model and then using this knowledge to feed another model and 
    generate the output.
    """
    lyrics = generate_rap_lyrics("gpt-3.5-turbo")
    logger.info(f"Lyrics: {lyrics}")
