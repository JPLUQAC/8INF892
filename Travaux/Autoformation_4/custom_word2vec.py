import tensorflow as tf
from tensorflow.keras import layers

class Custom_Word2Vec(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(Custom_Word2Vec, self).__init__()
        self.target_embedding = layers.Embedding(vocab_size,embedding_dim,name="w2v_embedding")
        self.context_embedding = layers.Embedding(vocab_size,embedding_dim)

    def call(self, pair):
        target, context = pair
        if len(target.shape) == 2:
            target = tf.squeeze(target, axis=1)
        word_emb = self.target_embedding(target)
        context_emb = self.context_embedding(context)
        dots = tf.einsum('be,bce->bc', word_emb, context_emb)
        return dots

    def custom_loss(x_logit, y_true):
        return tf.nn.sigmoid_cross_entropy_with_logits(logits=x_logit, labels=y_true)