# Cours 3 - 23 Janvier 2023

## Adaptive Linear Neurons

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

## Hyperparamètres
- Le _Learning rate_ et le nombre d'_epochs_ sont ce qu'on appel des hyperparamètres
- Pas de valeurs parfaits
- Learning rate trop haut peut empêcher de converger
- Un learning rate trop faible fera tourner l'algorithme longtemps (besoin de rouler un trop grand nombre d'epochs)
- Des méthodes exiswtent pour automatiquement caliber les hyperparamètres
- Discuter plus tard dans le cours

## Stochastic gradient descent
- Parfois iterative ou en-ligne
- Incrémentation des poids pour chaque échantillon de l'ensemble d'entraînement
- Il faut **absolument** mélanger nos données à chaque passe
- Approximation de l'algorithme du gradient
- Converge plus rapidement en général
- L'erreur contient plus de bruit
- Learning rate est souvent adaptatif avec SGD
- Dans l'exemple, à 10 epochs on voit qu'on a congergé

## Optimiseurs
- _Skipped_
- Pas encore d'optimiseurs idéal trouver
- Librairies (liens) dans les assétates
