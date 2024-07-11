'''
A zero-shot classifier refers to a classification model or system that can
 correctly categorize data into classes that it has not seen during training. 
'''

import pandas as pd
import numpy as np
from pathlib import Path
import json
import api
from logger import Logger
from sklearn.metrics import precision_score
from utils import (
    get_embedding,
    calc_cosine_similarity,
    calc_similarities,
    download_nltk_data,
    preprocess_text,
)


logger = Logger().get_logger()


def load_categories(dataset):
    categories = set()
    with open(dataset, 'r') as file:
        for line in file:
            data = json.loads(line)
            categories.add(data['category'])
    return list(categories)


def evaluate_precision(dataset, categories):
    '''Precision in a zero-shot classifier is useful in scenarios where
     false positives are costly or undesirable.
    '''
    df = pd.read_json(dataset, lines=True).head(20)

    y_true = []
    y_pred = []

    # Classify each sentence in the dataset
    for _, row in df.iterrows():        
        real_category = row['category']
        predicted_category = classify_sentence(row['headline'], categories)
        
        y_true.append(real_category)                
        y_pred.append(predicted_category)
        
        if real_category != predicted_category:
            logger.info(
            "😏 Incorrect prediction: "
            f"{row['headline'][:50]}...\n"
            f"Real: {real_category[:20]}\n"
            f"Predicted: {predicted_category[:20]}"
            )
        else:
            logger.info(
            "😀 Correct prediction: "
            f"{row['headline'][:50]}...\n"
            f"Real: {real_category[:20]}\n"
            f"Predicted: {predicted_category[:20]}"
            )

    return precision_score(
        y_true, 
        y_pred, 
        average='micro', 
        labels=categories
    )


def classify_sentence(sentence, categories):
    # Get the embedding of the sentence
    sentence_embedding = get_embedding(sentence)

    # Calculate the similarity score 
    similarity_scores = {}
    for category in categories:
        category_embeddings = get_embedding(category)
        similarity_scores[category] = calc_cosine_similarity(sentence_embedding, category_embeddings)

    # Return the category with the highest similarity score
    return max(
        similarity_scores, 
        key=similarity_scores.get
    )


# Evaluate the precision of the classifier
dataset = 'embedding/data/news.json'
categories = load_categories(dataset)
precision = evaluate_precision(dataset, categories)
logger.info(f"Precision: {precision}")
