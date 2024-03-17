import random
import pandas as pd

import tensorflow as tf

def cosine_similarity(a, b):
  mag_a = tf.sqrt(tf.reduce_sum(tf.multiply(a, a)))
  mag_b = tf.sqrt(tf.reduce_sum(tf.multiply(b, b)))
  return tf.reduce_sum(tf.multiply(a, b)) / (mag_a * mag_b)

# Load data into Dataframes
words = pd.read_csv('words.tsv',sep='\t')
vectors = pd.read_csv('vectors.tsv',sep='\t')

# Get the distance between different words
number_embeddings = len(vectors)
for i in range(20):
  one = random.randrange(0, number_embeddings)
  two = random.randrange(0, number_embeddings)

  embedding_one = vectors.iloc[one]
  embedding_two = vectors.iloc[two]

  distance = cosine_similarity(embedding_one, embedding_two)

  word_one = words.iloc[one]
  word_two = words.iloc[two]

  print("Cosine similarity between " + str(word_one[0]) + " and " + str(word_two[0]) + " is: " + str(distance))