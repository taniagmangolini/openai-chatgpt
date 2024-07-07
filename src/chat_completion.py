import sys
import logging
import api
from messages.questions import greeting, hannibal_question, storytelling
from messages.few_shots import (
    capitalize_task,
    format_numbers_task,
    seven_wonders_of_world_task,
    sci_fi_movies_2021,
)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__ == "__main__":

    api.show_available_models()

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", greeting).choices[0].message.content
    )

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", hannibal_question, max_tokens=70)
        .choices[0]
        .message.content
    )

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", storytelling, temperature=2.0)
        .choices[0]
        .message.content
    )

    stop_token = ["\n", "user:", "assistant:"]
    logger.info(
        api.create_chat_completion(
            "gpt-3.5-turbo", hannibal_question, stop_token=stop_token, max_tokens=100
        )
        .choices[0]
        .message.content
    )

    # Stream example

    response = api.create_chat_completion(
        "gpt-3.5-turbo",
        storytelling,
        temperature=2.0,
        max_tokens=100,
        stream=True,
        frequency_penalty=1.0,
    )
    for message in response:
        content = message.choices[0].delta.content
        if content:
            logger.info(content)

    # Few shots examples

    logger.info(
        api.create_a_few_shot_chat_completion_task("gpt-4", capitalize_task, 1.2)
    )

    logger.info(
        api.create_a_few_shot_chat_completion_task("gpt-4", format_numbers_task)
    )

    logger.info(
        api.create_a_few_shot_chat_completion_task(
            "gpt-4", seven_wonders_of_world_task, prefix="\n1."
        )
    )

    logger.info(
        api.create_a_few_shot_chat_completion_task(
            "gpt-3.5-turbo", sci_fi_movies_2021, prefix="\n1."
        )
    )

    logger.info(
        api.create_a_few_shot_chat_completion_task(
            "gpt-3.5-turbo",
            sci_fi_movies_2021,
            prefix="\n1.",
            stop_token=["4."],  # only the first, second and third movies
        )
    )
