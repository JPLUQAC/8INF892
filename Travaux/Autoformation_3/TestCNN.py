import PremierCNN
from tensorflow import keras
import numpy as np

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# Mise à l'echelle des images dans l'intervalle [0, 1]
train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255
train_images = np.expand_dims(train_images, -1)
test_images = np.expand_dims(test_images, -1)

# Convertir les vector en matrice binaire
train_labels = keras.utils.to_categorical(train_labels, 10)
test_labels = keras.utils.to_categorical(test_labels, 10)

cnn = PremierCNN.CNN(batch_size=128, epochs=15, input_shape=(28, 28, 1), n_output=10)

cnn.fit(train_images, train_labels)

cnn.evaluate(test_images, test_labels)
