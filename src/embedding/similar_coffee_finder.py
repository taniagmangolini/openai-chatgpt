import pandas as pd
import numpy as np
from pathlib import Path
import api
from logger import Logger
from utils import (
    get_embedding,
    calc_cosine_similarity,
    generate_embeddings_for_dataset,
    download_nltk_data,
    preprocess_text,
)


logger = Logger().get_logger()

coffee_embeddings = "embedding/data/simplified_coffee_embeddings.csv"

if not Path(coffee_embeddings).is_file():
    raw_dataset = coffee_embeddings.replace("_embeddings.csv", ".csv")
    generate_embeddings_for_dataset(
        raw_dataset=raw_dataset, column="review", preprocess=True
    )

# Using cosine similarity to find the word most similar to the user search term
df = pd.read_csv(coffee_embeddings)
df = df.assign(embedding=df["embedding"].apply(eval).apply(np.array))

# user search term
try:
    user_search = input("Enter a coffee name:")
    input_coffee_index = df[df['name'] == user_search].index[0]
    logger.info(f'Coffee index {input_coffee_index}')
except:
    print("Please enter a valid coffee name!")
    exit()

# Calculate the cosine similarity between 
# the input coffee's review and all other reviews
similarities = []
input_review_embedding = df.iloc[input_coffee_index, len(df.columns) - 1]
for review_embedding in list(df["embedding"].values):
    similarity = calc_cosine_similarity(
        input_review_embedding, 
        review_embedding
    )
    similarities.append(similarity)

# Get the indices of the most similar reviews (excluding the input coffee's review)
most_similar_indices = np.argsort(similarities)[-6:-1]

# Get the names of the most similar coffees
similar_coffee_names = df.iloc[most_similar_indices]['name'].tolist()

logger.info(f"According to the reviews, the most similar coffees to {user_search} are:")
logger.info(similar_coffee_names)
