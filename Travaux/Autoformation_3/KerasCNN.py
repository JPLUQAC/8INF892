import numpy as np
from tensorflow import keras
from keras import layers

class CNN(object):

  def __init__(self, batch_size, epochs, input_shape, n_output):

    self.epochs = epochs
    self.batch_size = batch_size

    self.model = keras.Sequential(
      [
          keras.Input(shape=input_shape),
          layers.Conv2D(8, kernel_size=(3, 3), activation="relu"),
          layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
          layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
          layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
          layers.MaxPooling2D(pool_size=(2, 2)),
          layers.Flatten(),
          layers.Dropout(0.5),
          layers.Dense(n_output, activation="softmax"),
      ]
  )

  def fit(self, x_train, y_train):
    self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    self.model.fit(x_train, y_train, batch_size=self.batch_size, epochs=self.epochs, validation_split=0.1)

  def evaluate(self, x_test, y_test):
    score = self.model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])