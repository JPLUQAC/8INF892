# Code de base fait par Kevin Bouchard, Ph.D
# Modifier par Jean-Philippe Larouche

import Perceptron as p
import pandas as pd
from sklearn.utils import shuffle

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df = shuffle(df)
print(df.iloc[0:25, :5].values) # Voir les 25 premieres lignes vu que c'est ceux qu'on utilise

y_train = df.iloc[0:25, 4].values
X_train = df.iloc[0:25, :4].values

ppn = p.Perceptron(eta=0.01, n_iter=50)
ppn.fit(X_train, y_train)

# Test
X_test = df.iloc[30, :4].values
print("Prediction : " + ppn.predict_class(X_test) + "\nActual : " + df.iloc[30, 4])