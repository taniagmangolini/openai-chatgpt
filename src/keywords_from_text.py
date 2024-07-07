import sys
import logging
from typing import Optional
from api import client
from messages.few_shots import keywords_task


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def generate_keywords_from_text(model, messages, temperature=0.2):
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature
    )
    return f"{response.choices[0].message.content}"


if __name__ == "__main__":
    logger.info(generate_keywords_from_text("gpt-3.5-turbo", keywords_task))
