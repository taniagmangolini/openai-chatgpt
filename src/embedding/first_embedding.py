import api
from logger import Logger


logger = Logger().get_logger()

"""
t the input (in our case, “I am a programmer”) must not exceed 8191 tokens in length. 
This limit could be different for other embeddings models. Given that 100 tokens roughly 
equate to 75 English words, the maximum input for the text-embedding-ada-002 model 
is approximately 6,143 words (8191 tokens x 0.75).
"""
result = api.create_embedding(
    model="text-embedding-ada-002",
    input = [
        "I am a programmer", 
        "I am a writer"
    ]
)


#logger.info(f"result: {result}")
for i, embedding in enumerate(result.data):
    logger.info(f"Embedding: {embedding}") #These floating points represent the embedding of the input text


"""
An embedding is a method of representing an object, like text, with an array of values.
It can be used as inputs for others models.

Output example:

CreateEmbeddingResponse(
    data=[
        Embedding(  #Each embedding is a list of floating-point numbers.
            embedding=[
                -0.016873637, 
                -0.019692589, 
                ..etc
            ], 
            index=0, 
            object='embedding'
        )
    ], 
    model='text-embedding-ada-002', 
    object='list', 
    usage=Usage(
        prompt_tokens=4, 
        total_tokens=4
    )
)
"""