import sys
import api
import logging
from typing import Optional
from messages.few_shots import keywords_task


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def generate_keywords_from_text(model, messages):
    response = api.create_a_few_shot_chat_completion_task(model, messages)
    return f"{response}"

if __name__ == "__main__":
    logger.info(generate_keywords_from_text("gpt-3.5-turbo", keywords_task))
