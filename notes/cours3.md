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

## Algorithmes
- On va seulement voir sur une petite partie car il en a une quantité énorme
  - Pendant un bout, tout l'industrie tentait de trouver le meilleurs algorithme
- L'objectif est de voir un portrait global et de comprendre le but de chaques classes d'algorithmes

### Paramétrique
- Avantages : Simple, apprentissage rapide, peu de données requises
- Inconvénients : Contrait à une forme, pour problèmes simples

### Non-paramétriques
- Avantages : Flexible, Puissant, Performant pour la prédiction
- Inconvénients : Surapprentissage, Plus lent, Plus de de données

### SVM
- Un des meilleurs algorithmes d'apprentissage automatique de base (une fois optimisé)
- Dans le perceptron, minimisation de l'erreur de classification
- Dans SVM, maximiser la marge entre les classes
  - Marge : Distance entre un hyperplan et les échantillons les plus près de ce plan (support vectors)

#### vs Logistic Regression
- Donnent des résultats similaires en pratique
- Logistic : Maximise les probabilités conditionnelles des échantillons
  - Plus sensible aux données aberrantes
  - Modèle plus simple
  - Plus facile à implémenter
  - Plus facile à mettre à jour
- SVM
  - Principalement préoccupé par les échantillons à la frontière des classes
  - Peu avatageux par rapport à logistic regression

#### Kernelisation
- Le SVM est tr`s populaire aussi parc qu'on peut facilement faire de la kernelisation (pas le seul)
- Truc du noyau est de créer des combinaisons non-linéaires des attributs originaux et de les projeter dans un espace à plus haute dimension
- Dans cette dimension, ils deviennent linéairement séparables

### KNN
- Choisir un nombre de voisins _k_ et une mesure de distance
- Trouver les _k_ voisions les plus proches de l'exemple à classer
- Faire un vote (majorité, majorité pondérée)
- On utilise généralement une distance de Minkowski
- Problème : on doit garder tous les exemples d'entraînement
  - Mémoire est un bottleneck
  - Fonctionne mal si la dimensionnalité est élevé
- Modèle non linéaire
  - mais très complexe

### Arbres de décision
- Utilise les attributs de l'ensemble de données afin d'apprendre une série de questions pour inférer les classes
- Commence à une racine et sépare les données sur l'attribut qui permet d'obtenir le plus grand **gain d'information**
- Répeter jsuqu'à ce que tous le sfeuilles soient pures (représentent une seule classe)
- **Faire attention au surapprentissage**
- Comment balancer l'apprentissage est souvent le grand défis
- Un des plus gros avantage est l'explicabilité et la transparence des modèles (XAI)
- Souffre cependant énormément du débalancement des classes
- Les principaux algorithmes sont:
  - Classification & Regression Trees (CART)
  - Iterative Dichotomiser (ID3)
  - C4.5
  - Very Fast Decision Trees (VFDT)
  - Chi-square Automatic Interaction Detector (CHAID)Multivaraite Adaptive Regression Splines (MARS)
  - Extremely Fast Decision Tree (EFDT) = VFDT++

## Surapprentissage (Overfitting)
- Modèle non-linéaires sont affectés
- High-variance

## Biais
- Le biais est le fait que des hyptho`ses simplificatrices sont formulées pour modéliser une population
- Haut biais:
  - Plus rapide pour l'apprentissage
  - Plus simples
  - Moins bonnes performances sur les problèmes complexes
- Affecte plus les algorithmes linéaires

## Variance
- La variance représente le changement de l'estimation de la fonction cible si les données d'entraînement changent
- Haute variance : Très influencé par les particularités des données
- Affecte plus les algorithmes non linéaires

## Bias-Variance Tradeoff
- Objectif de tous les algorithmes supervisés:
  - Biais faible et variance faible
  - Bon taux de prédicitons
- Le compromis se situe au niveau de la configuration des algorithmes

## Régularisation L2
- Un modèle qui permet de trovue un bon compromis Biais-Variance
- Peuit aider à prévenir le surapprentissage
- idée : introduire un nouveau biais pour pénaliser les valeurs extrêmes de podes
- Se définie par:
  - Gamma est le paramètre de reégularisation

## Régularisation L1
- Norme L1, somme des poids en valeur absolue (LASSO)
- Peut aussi servir à faire de la sélection de caractéristiques (feature selection) puisque certains poids tombent à 0
- Si la dimension m est plus grande que le nombre d'échantillon, on perd beaucoup de features

## Ensemble learning
- Un ensemble de classeurs faibles performent mieux qu'un seul très bon classeur

### Bagging
- Sous-ensemble du dataset pour l'entraînement
- Tire au sort un ensemble de donnée
  - Remet les données dans le _sac_ à chaque itération
  - Article scientifique démontre que prendre 2/3 des données est la meileure approche 
- Principaux algorithmes: RandomForest, Extremely Randomized Trees, Wagging

### Stacking
- Empile des classeurs
  - La premier couche entraîne la deuxième et ainsi de suite
- Chaque _stack_ peut être différent
  - Premier peut être _logistic regression_, deuxième est _Adaline_, etc.
- C'est un algorithme qui est très lents alors pas vraiment utilisé

### Boosting
- Exemple:
  - Maximisation de la fonction de coûts
  - On ajuste les poids, on entraîne un second calsseur
  - On ajuste les poids, on entraîne un troisième classeur
  - On combine les classeurs par vote
- Fonctionne pas bien avec des données bruiantes car le modèle va se concentrer juste sur eux avec le temps

### Adaboost
- Première version du boosting
- Voir la slide 42 du cours pour voir comment il fonctionne
- Vraiment le concept de base de boosting mais implémenté
- Permet de mettre un poids au vote pour aider

#### Variantes
- Real Adaboost : Calcule ses hypothèses faibles en optimisant directement les limites uspérieures des erreurs d'entraînement
  - Généralisation plus rapide d'Adaboost, les sorties sont des probabilités 
- Gental Adaboost : Limite le coefficient _petit alpha_ pour éviter les troop grandes valeurs
- SoftBoost, Interactive Boosting, ReweightBoost, Soft-LPBoost, RobustBoost
  - La plupart se concentrent sur la généralisation d'Adaboost
 
### Gradient boosting 
