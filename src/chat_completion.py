from logger import Logger
import api
from messages.questions import greeting, hannibal_question, storytelling
from messages.few_shots import (
    capitalize_task,
    format_numbers_task,
    seven_wonders_of_world_task,
    sci_fi_movies_2021,
)


logger = Logger().get_logger()


if __name__ == "__main__":

    api.show_available_models()

    logger.info(api.create_chat_completion("gpt-3.5-turbo", greeting))

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", hannibal_question, max_tokens=70)
    )

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", storytelling, temperature=2.0)
    )

    stop_token = ["\n", "user:", "assistant:"]
    logger.info(
        api.create_chat_completion(
            "gpt-3.5-turbo", hannibal_question, stop_token=stop_token, max_tokens=100
        )
    )

    # Stream example

    stream_response = api.create_chat_completion(
        "gpt-3.5-turbo",
        storytelling,
        temperature=2.0,
        max_tokens=100,
        stream=True,
        frequency_penalty=1.0,
    )
    for message in stream_response:
        for chunk in message.choices:
            content = chunk.delta.content
            if content:
                logger.info(content)

    # Few shots examples

    logger.info(api.create_chat_completion("gpt-4", capitalize_task, 1.2))

    logger.info(api.create_chat_completion("gpt-4", format_numbers_task))

    logger.info(
        api.create_chat_completion("gpt-4", seven_wonders_of_world_task, prefix="\n1.")
    )

    logger.info(
        api.create_chat_completion("gpt-3.5-turbo", sci_fi_movies_2021, prefix="\n1.")
    )

    logger.info(
        api.create_chat_completion(
            "gpt-3.5-turbo",
            sci_fi_movies_2021,
            prefix="\n1.",
            stop_token=["4."],  # only the first, second and third movies
        )
    )
