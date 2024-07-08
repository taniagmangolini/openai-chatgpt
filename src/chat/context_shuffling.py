import api
from logger import Logger
from messages.few_shots import (
    get_messages_for_prompt_and_behaviour
)


logger = Logger().get_logger()


if __name__ == "__main__":   
    """Context stuffing is a technique to give the model more context. 
    A context is a hint given to the model to guide it through user-defined patterns.
    Context stuffing can be used to influence the model’s response and can be useful 
    for give knowledge that is more recent than the data upon which the model was trained.
    In the first example, we give a specific phrase and ask the model what the role of the 
    word 'light' in that context.
    In the second example, the response about Apple be a company or a fruit can change
    according to the context supplied.
    """
    model = "gpt-3.5-turbo"

    prompt_a = """The light is red. Determine the part of speech of the word 'light'.\n\n"""
    prompt_b = """This desk is very light. Determine the part of speech of the word 'light'.\n\n"""
    prompt_c = """You light up my life. Determine the part of speech of the word 'light'.\n\n"""
    prompt_d = """He stepped light on the snow, trying not to leave deep footprints. Determine the part of 
    speech of the word 'light'.\n\n"""
    prompt_e = """Huawei:company; Google:company; Microsoft:company; Apple:"""  # returns company
    prompt_f = """Huawei:company; Google:company; Microsoft:company; Apricot:fruit; Orange:fruit; Apple:""" # returns fruit + company
    
    for prompt in [
        prompt_a, 
        prompt_b, 
        prompt_c, 
        prompt_d,
        prompt_e, 
        prompt_f
    ]:

        messages = get_messages_for_prompt_and_behaviour(prompt)
        result = api.create_chat_completion(model, messages)
        logger.info(f"result: {result}")
