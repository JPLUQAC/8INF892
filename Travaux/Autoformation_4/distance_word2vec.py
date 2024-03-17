import numpy as np
import random
import pandas as pd

import tensorflow as tf

def cosine_similarity(a, b):
  mag_a = tf.sqrt(tf.reduce_sum(tf.multiply(a, a)))
  mag_b = tf.sqrt(tf.reduce_sum(tf.multiply(b, b)))
  return tf.reduce_sum(tf.multiply(a, b)) / (mag_a * mag_b)

def euclidean_distance(a, b):
    sum_sq = np.sum(np.square(a - b))
    return np.sqrt(sum_sq)

def find_closest_word(target_vector_index, target_vector, vectors):
    cos_sim = -1
    index = 0
    for i in range(len(vectors)):
        if i != target_vector_index:
            tmp = cosine_similarity(target_vector, vectors.iloc[i])
            if tmp.numpy() > cos_sim:
                cos_sim = tmp
                index = i
    return index

# Load data into Dataframes
words = pd.read_csv('words.tsv',sep='\t')
vectors = pd.read_csv('vectors.tsv',sep='\t')

# Get the distance between different words
number_embeddings = len(vectors)
print("Running calculations on 50 differents word embeddings...")
for i in range(50):
    one = random.randrange(0, number_embeddings)
    embedding_one = vectors.iloc[one]

    for i in range(20):
        two = random.randrange(0, number_embeddings)
        embedding_two = vectors.iloc[two]

        cos_sim = cosine_similarity(embedding_one, embedding_two)
        euc_dis = euclidean_distance(embedding_one, embedding_two)

        word_one = words.iloc[one]
        word_two = words.iloc[two]

        print("***** " + str(word_one.iloc[0]) + " | " + str(word_two.iloc[0]) + " *****")

        print("Cosine similarity between is: " + str(cos_sim.numpy()))
        print("Euclidean Distance between is: " + str(euc_dis))

    index = find_closest_word(one, embedding_one, vectors)
    closest_word = words.iloc[index]
    print("The closest word to " + str(word_one.iloc[0]) + " is: " + str(closest_word.iloc[0]))