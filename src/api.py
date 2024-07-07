import os
import sys
import logging
from typing import Optional
from openai import OpenAI


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value


client = OpenAI(api_key=os.environ["API_KEY"], organization=os.environ["ORG_ID"])


def show_available_models():
    """Show all available models."""
    models = client.models.list()
    logger.info("Available models:")
    for model in models:
        logger.info(model.id)


def create_chat_completion(
    model,
    messages,
    temperature=1.0,
    prefix="",
    stop_token: Optional[list] = None,
    max_tokens=50,
    top_p=1,
    stream=False,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    n=1,
):
    """The text inputs to the models are referred to as "prompts".
    Chat models will take a list of messages as input and return a -generated message as output.
    They are not deterministic by default, but you can set params to make it more deterministic.
    Messages input must be an array of message objects, where each object has a
    role (either "system", "user", or "assistant") and content:

    - The system message (optional) helps set the behavior of the assistant. For instance: 'You are a movie expert.'
    - The user role represents the user and is used to send a message to the model.
    - This assistant role is optional and represents the AI model and is used to send a message to the user.

    Language models read and write text in chunks called tokens.
    For example, the string "ChatGPT is great!" is encoded into six tokens: ["Chat", "G", "PT", " is", " great", "!"].
    You pay by the input + output tokens (see the total_tokens in the response).

    The length of the output is determined by the API. To control the length of the output, you can use the max_tokens parameter.
    The max_token parameter consider the prompt + model tokens.
    This parameter is a number that depends on the model. For example, the max_tokens for the GPT-3.5-Turbo model is 4095.
    Even with a higher token count, the response may still be cut off. To avoid this, you can use the stop parameter.
    It is a list of stop strings. For instance, ['.', '\n', 'user:', 'assistant:']

    About the temperature parameter: Select a temperature value based on the desired trade-off between coherence
    and creativity for your specific application. The temperature can range is from 0 to 2.
    Lower values for temperature result in more consistent outputs (e.g. 0.2),
    while higher values generate more diverse and creative results (e.g. 1.0).
    When the model is too hot, it can generate words unrelated to the context. This is known as “hallucination”.

    top_p param can be an alternative to temperature for controlling the randomness of text generation in models like
    GPT-3 or GPT-4. The model will only consider the most probable next words that, added together, reach a certain
    cumulative probability (the top_p value). The default value is 1.0.
    If you set top_p to a high value (e.g., 0.95), the model might generate more unexpected and creative twists.
    If you set top_p to a lower value (e.g., 0.7), the story might be more straightforward and predictable.
    top_p computes the cumulative probability distribution, and cut off as soon as that distribution exceeds the value of top_p.
    For example, a top_p of 0.3 means that only the tokens comprising the top 30% probability mass are considered.
    Using both temperature and top_p is possible but not recommended.

    The model could takes our starter (prefix) and provides a suitable continuation.
    This powerful feature allows us to get specific outputs from the model without providing every detail;
    the model fills in the gaps based on its training.

    Streaming can be useful for applications where you want to display the output as it is generated.

    Param presence_penalty: how much the model penalizes repeated use of the same topic or terms within a response (diversity control).
    A higher presence penalty is useful to avoid redundancy.The default is 0.0.

    Param frequency_penalty: how much the model penalizes the repeated use of the same word or phrase (repetition control).
    This penalty encourages the model to use a wider vocabulary and prevents it from repeating itself. The default is 0.0.

    If you want more than one result, you can use the n parameter. So the model will return more choices.

    Returns a ChatCompletion object. For instance:

    ChatCompletion(
        id='chatcmpl-8jvdNPNv7923lcVHtn3zjNt3GqkAY',
        choices=[
            Choice(
                finish_reason='stop', # stop, length (exceeded max tokens or limit), function_call, content_filter (was flagged) or null (api has more tokens to generate)
                index=0,
                logprobs=None, # probabilities for each token
                message=ChatCompletionMessage(
                    content='Hello! How can I help you today?',
                    role='assistant',
                    function_call=None, # function used to generate it
                    tool_calls=None
                )
            )
        ],
        created=1705956997,
        model='gpt-3.5-turbo-0613',
        object='chat.completion',
        system_fingerprint=None, # backend configuration of an OpenAI model
        usage=CompletionUsage(
            completion_tokens=9, # number of tokens generated by the model (output)
            prompt_tokens=22, # input tokens
            total_tokens=31
            )
        )
    """
    logger.info(f"Performing a chat completion with {model}...")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop_token,
        top_p=top_p,
        stream=stream,
        n=n,
        # response_format={ "type": "json_object" }
    )

    if stream:
        return response

    if n == 1:
        return f"{prefix} {response.choices[0].message.content}"
    return [f"{prefix} {choice.message.content}" for choice in response.choices]
