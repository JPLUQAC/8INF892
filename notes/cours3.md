# Cours 3 - 23 Janvier 2023

## Adaptive Linear Neurons (revue du cours précédent)

### Adaline
- Type de NN simple couche
- MàJ des poids selon une fonction d'activation linéaire
- Fonction d'activation linéaire est simplement la fonction d'identité de l'entrée nette
- Sert à mettre à jour les pods
- Élément similaire à la fonction Heaviside (parfois nommé _Quantizer_) permet la prédiction de la classe
- Sorties sont des valeurs continues (plutôt que binaire)

### Fonction de coûts
- Clé en ML : optimisation d'une fonctione objective (cost function)
- Pas un cours d'optimisation mais nous devrons comprendre quelques éléments
- Pour Adaline, fonction de coûts à minimiser
  - Apprendre les poids en tant que _Sum of Suqared Errors_ (SSE) entre les sorties et les vraies classes

### Algorithme du gradient
- _Gradient descent_
  - Permet de faire l'optimisation
- Regarde la pente des états voisins
  - Bouge dans la direction la plus abrupte
  - Rappel : Trouvée par la dérivée partielle

### Résumé 
- Même si la règle d'apprentissage ressemble à celle du perceptron, c'est un nombre réel
  - Perceptron c'est un entier naturel
- La MàJ des poids se fait sur le dataset en entrier
  - Incerémental dans le perceptron (instance par instance)
- L'algorithme du gradient bénéficie du feature scaline
  - Calcul est plus rapide
  - sklearn.preprocessing.scale
- Voir le code en POython de Adaptive Linear Neuron   

### Hyperparamètres (revue du cours précédent)
- Le _Learning rate_ et le nombre d'_epochs_ sont ce qu'on appel des hyperparamètres
- Pas de valeurs parfaits
- Learning rate trop haut peut empêcher de converger
- Un learning rate trop faible fera tourner l'algorithme longtemps (besoin de rouler un trop grand nombre d'epochs)
- Des méthodes exiswtent pour automatiquement caliber les hyperparamètres
- Discuter plus tard dans le cours

### Stochastic gradient descen
- Parfois iterative ou en-ligne
- Incrémentation des poids pour chaque échantillon de l'ensemble d'entraînement
- Il faut **absolument** mélanger nos données à chaque passe
- Approximation de l'algorithme du gradient
- Converge plus rapidement en général
- L'erreur contient plus de bruit
- Learning rate est souvent adaptatif avec SGD
- Dans l'exemple, à 10 epochs on voit qu'on a congergé

## Optimiseurs (revue du cours précédent)
- _Skipped_
- Pas encore d'optimiseurs idéal trouver
- Librairies (liens) dans les assétates
  
## Algorithmes
- On va seulement voir sur une petite partie car il en a une quantité énorme
  - Pendant un bout, tout l'industrie tentait de trouver le meilleurs algorithme
- L'objectif est de voir un portrait global et de comprendre le but de chaques classes d'algorithmes

## Scikit-learn
- Libraire les plus faciles à utiliser pour _data mining_ et _data analysis_
- Open source
- Construit sur _Numpy_, _SciPy_ et _matplotlib_
- Large variété d'algorithmes et de méthodes d'optimisation de ceux-ci
  - Fonctions de traitement des données
  - Fonctions d'évaluation
- `import train_test_split` pour facilement faire un entraînement
- Standardisation des attributs
- Perceptron supporte déjà le multi classes dans SciKit via One vs All
- `import Perceptron` pour utiliser le perceptron

## Logistic Regression
- Similaire au Perceptron et à Adaline
- Classification binaire
- Très populaire, peut utiliser la stratégie One vs All
- Modèle probabiliste
- Fonction d'activation est le Sigmoid

### Odds ration
- Probabilité qu'un évènement se produise

### Fonction d'activation
- Prédire les probabilités qu'un échantillon appartienne à une classe spécifique
- C'est la fonction inverse, la fonction sigmoide (ou la fonction logistique!)
- z est la somme nette

### Interprétation
- La fonction d'activation tend vers:
  - 1 lorsque z tend vers l'infinie
  - 0 lorsque z tend vers moins l'infinie
- Z est interprété comme la probabilité qu'un échantillon appartienne à une classe spécifique
- On peut utiliser un Quantizer comme avec Adaline

### Apprentissage des poids
- Sum-Squared-Error (SSE) en tant que fonction de coûts
  - On a minimisé pour apprendre
- Fonction de coûts pour Logistic Regression
  - La probabilité à maximiser en supposant que les échantillons de notre dataset sont indépendants
  - Plus facile d'utiliser les logarithmes (fonction Log-Likelyhood)
- Les logs permettent d'éviter un _underflow_ (soupassement arithmétique)
- On transforme le produit en somme (plus facile à dériver)
- On peut optimiser de la même façon qu'avec Adaline en dérivant pour trouver le gradient
  - Attention : Il faut utiliser gradient ascent avec la fonction (ou inverser la fonction, voir slide 15 leçon #3)   
