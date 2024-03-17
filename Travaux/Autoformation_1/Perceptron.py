import numpy as np

class Perceptron(object):
    # Classe creer par Kevin Bouchard, Ph.D
    # Modifier par Jean-Philippe Larouche
    # Strategie multi-classes : One-Vs-All

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        self.class_weight_dictionary = {} # Chaque classe unique va avoir des poids : Dictionnaire

    def fit(self, X, y):
        classes = np.unique(y) # Obtenir toutes les classes

        # Entrainer un perceptron pour chaque classe
        for unique_class in classes:
            y_train = np.where(y == unique_class, -1, 1)
            w_ = np.zeros(1 + X.shape[1])
            self.errors_ = []
            
            print("Poids:", w_)

            for _ in range(self.n_iter):
                errors = 0
                for xi, target in zip(X, y_train):
                    update = self.eta * (target - self._predict(xi,w_))
                    print("Update = ", self.eta, " * (",target," - ", self._predict(xi,w_), ") = ", update)
                    print("Poids: ", w_[1:], " + ", xi, " * ", update, " = ", end = ' ')
                    w_[1:] += update * xi
                    print(w_[1:])

                    w_[0] += update
                    errors += int(update != 0.0)
                self.errors_.append(errors)
                print("ERREURS: ", errors)
            self.class_weight_dictionary[unique_class] = w_

    def _net_input(self, X, w_):
        """Calculate net input"""
        print("Z=", w_[0], "*1+", w_[1:], "*", X, " = ", np.dot(X, w_[1:]) + w_[0])
        return np.dot(X, w_[1:]) + w_[0]

    def _predict(self, X, w_):
        """Return class label after unit step"""
        return np.where(self._net_input(X, w_) >= 0.0, 1, -1)
    
    def predict_class(self, X):
        class_scores = {} # Chaque classe a un score : Dictionnaire

        # Aller chercher le score pour chaque percepton et l'ajouter au dictionnaire
        for unique_class, weight in self.class_weight_dictionary.items():
            class_scores[unique_class] = self._net_input(X, weight)

        return max(class_scores, key=class_scores.get) # Retourne la classe qui "fit" le mieux


# class _perceptronBase(object):
#     # Classe creer par Kevin Bouchard, Ph.D

#     def __init__(self, eta=0.01, n_iter=10):
#         self.eta = eta
#         self.n_iter = n_iter

#     def fit(self, X, y):
#         self.w_ = np.zeros(1 + X.shape[1])
#         self.errors_ = []

#         print("Poids:", self.w_)

#         for _ in range(self.n_iter):
#             errors = 0
#             for xi, target in zip(X, y):
#                 update = self.eta * (target - self.predict(xi))
#                 print("Update = ", self.eta, " * (",target," - ", self.predict(xi), ") = ", update)
#                 print("Poids: ", self.w_[1:], " + ", xi, " * ", update, " = ", end = ' ')
#                 self.w_[1:] += update * xi
#                 print(self.w_[1:])

#                 self.w_[0] += update
#                 errors += int(update != 0.0)
#             self.errors_.append(errors)
#             print("ERREURS: ", errors)
#         return self

#     def net_input(self, X):
#         """Calculate net input"""
#         print("Z=", self.w_[0], "*1+", self.w_[1:], "*", X, " = ", np.dot(X, self.w_[1:]) + self.w_[0])
#         return np.dot(X, self.w_[1:]) + self.w_[0]

#     def predict(self, X):
#         """Return class label after unit step"""
#         return np.where(self.net_input(X) >= 0.0, 1, -1)


# class Perceptron(object):
#     # Classe creer par Jean-Philippe Larouche
#     # Strategie multi-classes : One-Vs-All

#     def __init__(self, eta=0.01, n_iter=10):
#         self.eta = eta
#         self.n_iter = n_iter
#         self.perceptrons_dictionary = {} # Chaque classe unique va avoir un perceptron : Dictionnaire
    
#     def fit(self, X, y):
#         classes = np.unique(y) # Obtenir toutes les classes

#         # Entrainer un perceptron pour chaque classe
#         for unique_class in classes:
#             y_train = np.where(y == unique_class, -1, 1)
#             perceptron = _perceptronBase(self.eta, self.n_iter)
#             perceptron.fit(X, y_train)
#             self.perceptrons_dictionary[unique_class] = perceptron

#     def predict(self, X):
#         class_scores = {} # Chaque classe (perceptron) a un score : Dictionnaire

#         # Aller chercher le score pour chaque percepton et l'ajouter au dictionnaire
#         for unique_class, percepton in self.perceptrons_dictionary.items():
#             class_scores[unique_class] = percepton.net_input(X)

#         return max(class_scores, key=class_scores.get) # Retourne la classe qui "fit" le mieux
    