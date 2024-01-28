import Perceptron as p
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset (code du site UCI)
dry_bean_dataset = fetch_ucirepo(id=602) 
  
# data (as pandas dataframes) (code du site UCI)
X = dry_bean_dataset.data.features 
y = dry_bean_dataset.data.targets

# (code de la documentation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convertir les donnees pour notre perceptron 
X_train = X_train.iloc[0:50].values
y_train = y_train.iloc[0:50].values

# Train
ppn = p.Perceptron(eta=0.01, n_iter=50)
ppn.fit(X_train, y_train)

# Test
print("Prediction : " + ppn.predict_class(X_test.iloc[5]) + " Actual : " + y_test.iloc[5])