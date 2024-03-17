from sklearn.linear_model import Perceptron
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

# Train
ppn = Perceptron(eta0=0.01 ,max_iter=50)
ppn.fit(X_train, y_train)

# Test
y_pred = ppn.predict(X_test)
print("Prediction : " + y_pred[5] + " Actual : " + y_test.iloc[5])