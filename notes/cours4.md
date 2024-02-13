# Cours 4 - 30 Janvier 2024

# Rappel
- Bagging : Utiliser l'aléatoire pour améliorer la performance
- Stacking : Aligner successivement plusieurs couche de classeur afin de tirer avantage de la transformation des données fait à chaque couche

# Graident Boosting
- Similaire à Adaboost
- Même idée que l'apprentissage par ensemble
- Utilisé une fonction d'erreur (ex: fonction d'erreur au carré)
- Méthode statistique
- À chaque cycle de boosting, on va entraîne un arbe via un ensemble de donnée puis calcucler une erreur. On utilise ensuite l'erreur pour entraîner un arbre gradient
- Existe dans scikit-learn

## Variants principales
- Histogram-Based Gradient Boosting
- XGBoost (open-source)
- CatBoost

# Deep Learning
- La tendance la plus populaire en apprentissage automatique
- S'agit d'un ensemble d'algorithmes développés pour l'entraînement de réseau de neurons artificiels à plusieurs couches
- En 1986 que l'intérêt des NN reprend avec la découverte de l'algorithme **backpropagation** qui permet l'entraînement de réseaux multicouches plus facilement
- **State-of-the-art** pour les problèmes exploitant des données complexe (images, voix, textes)
- L2 pour réduire le surapprentissage

## Multiples couches
- Nos NN sont cimple couche, mêmne s'il y a une couche d'entrées et une de sorties à cause du lien unique qui les lie
- On peut ajouter une couche cachée de neurones pour former un réseau de neurones multicouche à propagation avant (multi-layer feed forward NN)
- Les neurones de la couche cachée sont complètement connectés à la couche d'entrées et à la couche de sortie
- Si + d'un niveau caché, alors besoin des techniques du **deep learning**

## Perceptron Multicouche
- Une unité dans la couche de sortie permet de faire de la classification binaire
- À l'aide de la représentation de classe par vecteur **one-hot**, on peut passer aux problèmes multiclasses
  - Contrairement à la représentation de classe en entier, les one-hot ne cause pas de problèmes avec les algorithmes basés sur des distances
 
### Propagation Avant
- La propagation avant permet de calculer la ou les sorties du réseau multicouche
- Puisque notre réseau est complètement connecté, nous calculons l'activation d'une untié (voir slide 10 pour fonction)
- Chaque couche sert d'entrée à la couche suivante sans qu'il n'y ait de boucle
  - Ce n,est pas le cas dans un _recurrent neural network_ où il y a une boucle
  - Verrons les modèles avec des boucles plus tard
- Même si on nomme ce modèle _multi-layer perceptron_, les ocuches sont composées d'unitées sigmoids et non pas de perceptrons
  - De plus, les valeurs retournées par les unités sont continues (0..1)
  - Nous n'utiliserons plus le fameux quantizer en deep learning
- Nous utiliserons une notation plus compacte pour l'activation
- On peuit généraliser aux n échantillons

## Exemple - Classfication de chiffres
- Problème bien connu et "simple"
- Dataset MNIST
  - 60k images d'entraînement
  - 10k images de tests
  - Les images sont les chiffres 0 à 9 écrit à la main
  - Très utile d'avoir ce dataset à porté de main
  - Nos modèles devrait avoir 94-95% de précision
- Long à rouler
- Intéressant de bien le rouler nous mêmes (avec modification) pour comprendre
- Il y a une version Tensorflow sur moodle (pas démontré)
- Va faire partie du deuxième travail d'autoformation

## Fonction de coûts
- Voir les slides, spécifique à l'exemple
