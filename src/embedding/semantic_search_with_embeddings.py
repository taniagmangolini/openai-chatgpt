import pandas as pd
from pathlib import Path
import api
from logger import Logger
from utils import get_embedding, calc_cosine_similarity, generate_embeddings_for_dataset
import numpy as np


logger = Logger().get_logger()


word_embeddings = "embedding/data/words_embeddings.csv"

if not Path(word_embeddings).is_file():
    raw_dataset = word_embeddings.replace("_embeddings.csv", ".csv")
    generate_embeddings_for_dataset(raw_dataset, "text")


df = pd.read_csv(word_embeddings)
df["embedding"] = (
    df["embedding"]
    .apply(
        eval  # applying eval to each element will convert the string representation of lists or arrays into actual Python list objects.
    )
    .apply(
        np.array  # after converting the string representations to lists, this second apply call converts these lists into numpy arrays
    )
)

# user search term
user_search_embedding = input("Enter a search term: ")
logger.info(f"Search term: {user_search_embedding}")

# embeddings for the user search term
user_search_embedding = get_embedding(user_search_embedding)

# Using cosine similarity to find the word most similar to the user search term
df = df.assign(
    similarity=lambda x: x["embedding"].apply(
        lambda col: calc_cosine_similarity(col, user_search_embedding)
    )
).sort_values(by="similarity", ascending=False)

logger.info(df.head(10))
