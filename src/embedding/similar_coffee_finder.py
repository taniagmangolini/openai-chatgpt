import pandas as pd
import numpy as np
from pathlib import Path
import api
from logger import Logger
from utils import (
    get_embedding,
    calc_cosine_similarity,
    calc_similarities,
    generate_embeddings_for_dataset,
    download_nltk_data,
    preprocess_text,
)


logger = Logger().get_logger()

coffee_embeddings = "embedding/data/simplified_coffee_embeddings.csv"

if not Path(coffee_embeddings).is_file():
    raw_dataset = coffee_embeddings.replace("_embeddings.csv", ".csv")
    generate_embeddings_for_dataset(raw_dataset=raw_dataset, columns=["name", "review"])

# Using cosine similarity to find the word most similar to the user search term
df = pd.read_csv(coffee_embeddings)
df = df.assign(review_embedding=df["review_embedding"].apply(eval).apply(np.array))
df = df.assign(name_embedding=df["name_embedding"].apply(eval).apply(np.array))


# user search term
try:
    user_search = input("Enter a coffee name:")
    input_coffee_index = df[df["name"] == user_search].index[0]
    logger.info(f"Coffee index {input_coffee_index}")
except:
    logger.info(
        f"We could not find {user_search}. We will search for the most similar one..."
    )
    # Calculate the cosine similarity between the input coffee's name and 
    #all other names and get the higher similarity
    input_name_embedding = get_embedding(user_search)
    names_similarities = calc_similarities(
        input_name_embedding, list(df["name_embedding"].values)
    )
    name_higher_similarity_value = max(names_similarities)
    input_coffee_index = names_similarities.index(name_higher_similarity_value)
    input_coffee_name = df.iloc[input_coffee_index, 1]
    logger.info(
        f"The most similar coffee found is {input_coffee_name} with {name_higher_similarity_value} % of similarity"
    )


# Calculate the cosine similarity between
# the input coffee's review and all other reviews
input_review_embedding = df.iloc[input_coffee_index, len(df.columns) - 1]
review_similarities = calc_similarities(
    input_review_embedding, list(df["review_embedding"].values)
)


# Get the indices of the most similar reviews (excluding the input coffee's review)
most_similar_indices = np.argsort(review_similarities)[-6:-1]

# Get the names of the most similar coffees
similar_coffee_names = df.iloc[most_similar_indices]["name"].tolist()

logger.info(f"According to the reviews, the most similar coffees to {user_search} are:")
logger.info(similar_coffee_names)
