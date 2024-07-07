import sys
import api
import logging
from typing import Optional
from messages.few_shots import (
    get_messages_for_generate_keywords_from_text_task,
    get_messages_for_generate_hashtags_from_text_task,
    get_messages_for_tweet_generation_task,
)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def generate_keywords_from_text(model, messages):
    """Chat completion task to extract keywords from a text."""
    keywords = api.create_chat_completion(model, messages)
    return f"{keywords}"


def create_hashtags(model, messages):
    """Chat completion task to generate hashtags from a text"""
    hashtags = api.create_chat_completion(
        model,
        messages,
        max_tokens=100,
        temperature=0,
        stop_token=["\n", "assistant:", "user:"],
    )
    logger.info(f"Hashtags {hashtags}")
    return hashtags


def create_tweet(model, text, n):
    """Chat completion task to create a tweet using sequential prompt chaining.
    The tweet has a 280-character limit.
    A common issue with LLMs like GPT-4 is their tendency to disregard user-defined limits.
    To overcome this, the following strategy will be applyed:
    - a low temperature (small creativity)
    - examples of tweets will be supplied to the model
    - we will generate n tweets and select the first that has the expected size.
    """
    hashtags = create_hashtags(
        model, get_messages_for_generate_hashtags_from_text_task(text)
    )

    tweets = api.create_chat_completion(
        model, get_messages_for_tweet_generation_task(text, hashtags), n=n
    )
    for tweet in tweets:
        if len(tweet) <= 280:
            return tweet


if __name__ == "__main__":

    TEXT = (
        "The first programming language to be invented "
        "was Plankalkül, which was designed by Konrad "
        "Zuse in the 1940s, but not publicly known until "
        "1972 (and not implemented until 1998). The first "
        "widely known and successful high-level programming "
        "language was Fortran, developed from 1954 to 1957 "
        "by a team of IBM researchers led by John Backus. "
        "The success of FORTRAN led to the formation of "
        "a committee of scientists to develop a "
        '"universal" computer language; the result of '
        "their effort was ALGOL 58. Separately, John McCarthy "
        "of MIT developed Lisp, the first language with "
        "origins in academia to be successful. With the "
        "success of these initial efforts, programming "
        "languages became an active topic of research "
        "in the 1960s and beyond."
        "The first programming language to be invented "
        "was Plankalkül, which was designed by Konrad "
        "Zuse in the 1940s, but not publicly known until "
        "1972 (and not implemented until 1998). The first "
        "widely known and successful high-level programming "
        "language was Fortran, developed from 1954 to 1957 "
        "by a team of IBM researchers led by John Backus. "
        "The success of FORTRAN led to the formation of "
        "a committee of scientists to develop a "
        '"universal" computer language; the result of '
        "their effort was ALGOL 58. Separately, John McCarthy "
        "of MIT developed Lisp, the first language with "
        "origins in academia to be successful. With the "
        "success of these initial efforts, programming "
        "languages became an active topic of research "
        "in the 1960s and beyond."
    )

    messages = get_messages_for_generate_keywords_from_text_task(TEXT)
    keywords = generate_keywords_from_text("gpt-3.5-turbo", messages)
    logger.info(keywords)

    tweet = create_tweet("gpt-3.5-turbo", TEXT, n=2)
    logger.info(f"Tweet: {tweet}")
