from sklearn.linear_model import Perceptron
import pandas as pd
from sklearn.utils import shuffle

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df = shuffle(df)
print(df.iloc[0:25, :5].values) # Voir les 25 premieres lignes vu que c'est ceux qu'on utilise

y_train = df.iloc[0:25, 4].values
X_train = df.iloc[0:25, :4].values

ppn = Perceptron(eta0=0.01 ,max_iter=50)
ppn.fit(X_train, y_train)

X_test = df.iloc[25:31, :4].values
y_pred = ppn.predict(X_test)
print("Prediction : " + y_pred[5] + "\nActual : " + df.iloc[30, 4])