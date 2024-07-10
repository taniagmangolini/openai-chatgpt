"""
In the field of Natural Language Processing (NLP), cosine similarity is a commonly used metric to measure the similarity between documents.
it calculates the cosine of the angle between two vectors projected in a multi-dimensional space. This metric examines the angle between two
vectors and compares them. The result is a number between -1 and 1. If the vectors are identical, the result is 1. 
If the vectors are completely different, the result is -1. If the vectors are at a 90-degree angle, the result is 0.
"""

import numpy as np
from numpy.linalg import norm
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity

# define two vectors
A = np.array([2, 3, 5, 2, 6, 7, 9, 2, 3, 4])
B = np.array([3, 6, 3, 1, 0, 9, 2, 3, 4, 5])

# calculate the cosine similarity using NumPy
cosine_np = np.dot(A, B) / (norm(A) * norm(B))

# print the cosine similarity
print(f"Cosine Similarity between A and B: {cosine_np}")


# calculate the cosine similarity using scipy
cosine_sc = 1 - spatial.distance.cosine(A, B)

# print the cosine similarity
print(f"Cosine Similarity between A and B: {cosine_sc}")

# calculate the cosine similarity using sklearn
cosine_sk = cosine_similarity([A], [B])

# print the cosine similarity
print(f"Cosine Similarity between A and B: {cosine_sk[0][0]}")
