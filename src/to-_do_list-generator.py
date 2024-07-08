import api
import sys
import math
from logger import Logger
from messages.few_shots import (
    get_messages_for_prompt_and_behaviour,
)


logger = Logger().get_logger()


try:
    number_of_tasks = int(sys.argv[1])
    topic = sys.argv[2]
except:
    print(
        """
Please provide the number of tasks followed by
the desired topic.
Examples: 
  python src/app.py 5 "run 10 Km"
  python src/app.py 3 "get a good job"
"""
    )
    exit()

# A helpful rule of thumb is that one token generally corresponds to 4 characters of text for common English text. 
# This translates to roughly 3/4 of a word (so 100 tokens= 75 words).

prompt_tokens = math.ceil(len(topic)/4)
TOKENS_PER_TASK = 50
max_tokens = number_of_tasks * TOKENS_PER_TASK + prompt_tokens
logger.info(f"Prompt tokens {prompt_tokens}, Max tokens {max_tokens}")

prompt = f"Create a to-do list to {topic} \
\
Task 1: \
"

logger.info(f"Building a {number_of_tasks} items to-do list to {topic}...")

stop_token = [f"Task {number_of_tasks + 1}:", "assistant:", "user:"]

messages = get_messages_for_prompt_and_behaviour(prompt)
to_to_list = result = api.create_chat_completion(
    "gpt-3.5-turbo", messages, stop_token=stop_token, max_tokens=max_tokens
)

logger.info(f"To do list: {to_to_list}")
