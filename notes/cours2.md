# Cours 2 - 16 Janvier 2024

# Introduction
- Suite au dernier cours
- **Caractéristiques = features**
- Ce n'est pas souvent discuté mais habituellement on va ré-entraîner un modèle sur la totalité des données avant de le mettre en production
  - Si nous avons bien faite notre méthodologie, il devrait avoir la même performance dans le pire des cas et une meilleure performance dans le meilleur des cas 

## Types d'apprentissage
- Divisé en fontion du _feedback_
- Valeur continue : On parle de regression
  - Analyse de regression
- Faire de l'etiquettage de donnée n'est pas facile
  - Demande beaucoup de temps et de ressource 

### Supervisé
- Plus facile à utiliser
- Les données sont étiquettés
- Les données sont _classés_ : **Classification**
- Données X pour faire une prédiction Y

### Semi-supervisé
- On va en parler beaucoup, très utile
- Très large
- Inclus toutes les formats ou nous avons un étiquettage partiel
- Apprentissage actif : Ensemble d'entraînement et nous allons utilisés une rétro-action de nous utilisateurs pour continuer d'entraîner
  - Penser à Google Translate
  - Va être utiliser par des gens
  - Incertitude est introduit (user generated content)
    - Utiliser des systèmes de niveau de confiance pour pondérer le contenu de l'utilisateur
- Apprentissage par groupe : On a des données sans être certain de nos étiquettes pour chaque de donnée mais nous savons ce qui existe dans les données

### Non-supervisé
- Aucun étiquette
- Difficile de s'assurer que les résultats de notre modèle est satisfesant
- On cherche souvent plus à faire sortir des relations

### Renforcement
- Ressemble beaucoup au supervisé
- Essaie d'associer nos données à des recompenses
- Peut utiliser du supervisé pour faire du renforcement et vice-versa
- Nous voulons que cela soit intéractif
- Beaucoup utilisé en jeux vidéo

## Tâches de l'apprentissage
- Classification : Sorties constituent un ensemble fini de valeurs catégoriques
  - Deep learning permet un pas vers la généralisation dans le sense ou un algorithme peut détecter un objet qui n'est pas dans ses classes (nécessite une deuxième source d'information) 
- Régression : Les sorties représentent un ensemble de valeurs continues
  - Permet la prédiction 
  - Ex: Tente de faire une fonction avec X pour prédire Y
- Regroupement (clustering) : Tenter de regrouper des éléments similaires ensemble et de différencier le plus possible les groupes
  - Pas d'étiquettes
  - Comment on évalue le modèle : Mesure de performance, c'est le défis!
- Renforcement : Tente d'améliorer une fonction d'agent pas l'expérience
  - Prends une décision par rapport à l'état
  - Une récompenses peut être positif ou négative
- Réduction de dimensionnalité (représentation de connaissance) : Réduction du nombre de variables de façon à n'obtenir que les principales
  - Extraire des caractéristiques
  - Sélectionner des caractéristiques
  - Sert souvent aux autres méthodes de ML
  - PCA : Principale component analysis
    - Très vieux comme algorithme 

 ## Ensembles de données
 - Données d'apprentissage : Base de données ou un ensemble de données structurés ne peuvent pas directement être utilisés pour l'apprentissage. Nous voulons plutôt des vecteurs d'attributs
 - Vecteur perds l'information spatiale
 - Datasets :
   - 10 000 sur kaggle
   - 622 sur UCI ML repository
   - Beaucoup d'autres (voir la slide)
   - Google a un moteur de recherche de dataset
   - Facile aujourd'hui trouver des datasets

## Préparation des données
 - Dans la vraie vie les données sont imparfaites alors il faut les traités

### Balancement des données
- Certain algorithme, tel que les Random Forest, ne fonctionne pas bien lorsque les données sont mal balancées
  - Penser aux biais
- Phénomène qui se produit lorsque la proportion d'exemples de chaque classe est très différent (Grand écart)
- Les classes avec un plus grand nombre d'échantillons seront favorisées
- Under sampling et over sampling sont des stratégies qui peuvent être intéressant dans certains contextes
- Génération de donnée synthétique 

### Normalisation des données
- On parle souvent de mise à l'échelle car les valeurs sont sur un différentes plages de nombres
  - Ex: Âge et salaire
  - Souvent on va mettre tous les plages entre 0 et 1 car c'est beaucoup plus simple 
- Plusieurs algorithmes sont influencé dans la création de leur modèle part les échelles de valeurs
- Certains algorithmes apprennent bien moins vite

#### Normalisation
- Mise à l'échelle d'un vecteur avec sa norme
- Algorithme classique est un  _MinMaxScaler_
  - Version absolue et non-absolue
- Normalisation L1 et L2
  - Similaire mais en termes de vecteurs afin qu'ils aient une norme unitaire plutôt que par caractéristique
  - Éviter le surapprentissage
- Plusieurs algorithmes sont disponbiles sur scikit-learn

## Processus générique du ML
1. Preprocessing
2. Apprentissage
3. Évaluation
4. Prédiction

# Neurone Artificielle
- Neurone fondée sur la neurone biologique (1943)
- Transmeettre des signeux électriques et chimiques
  - Entrées et sorties 

## Perceptron
- Rosenblatt 1957
- Modèle de base
- Pas très utilise aujourd'hui mais très pratique pour apprendre
- Apprendre les poids optimaux à multiplier avec les entrées afin de déterminer si le neurone s'active ou non
  - Utilise pour la classfication binaire (ML supervisé) : Deux classes
- Z est l'entrée nette composé d'une combinaison linéaire d'entrées x et de poids w (somme pondérée)
- La classification se définie par une fonction d'activation avec un threshold
- Simple équation linéaire
- Nombre de caractéristiques = nombre de paramètres
- Fonction d'activation s'appel _Heaviside_
  - Fait partie de ce qu'on appel la fonction _stepwise_ aujourd'hui
- On essaie d'apprendre notre seuil d'activation
  - On l'ajoute en paramètre
  - X zéro est toujours égale à 1 pour ajouter notre seuil d'activation comme paramètre

### Fonctionnement de l'apprentissage
1. Initialisation des poids à 0 (ou petit nombre aléatoire)
2. Pour chaque exemple d'entrainement X à la i
  1. Calculer la sortie estimée y à la i
  2. Mettre à jour les poids
- n est le fameux _learning rate_ entre 0.0 et 1.0
- Voir les slides 7 et 8
- Le poids ne change pas si la prédiction est correct
- **Pas d'erreur, pas d'apprentissage**

### Bilan
- Si ce n'est pas séparable linéairement, Perceptron MàJ à l'infini
  - Nombre max des passes à travers l'ensembles (epochs)
- Si la fonction est séparable linéairement, le Perceptron va s'arrêter seul car il ne feras plus d'erreur
- Passe instance par instance puis lorsque terminer on recommence une passe instance par instance jusqu'à ce que la condition d'arrêt soit atteninte
  - Un _epoch_ c'est une passe sur le dataset en entier

## Adaptive Linear Neuron : Adaline
- MàJ des poids selon une fonction d'activation linéaire
  - Simplement la fonction d'identité de l'entrée nette
- Les sorties sont des valeurs continues plutôt que binaire
- Très similaire au Perceptron
- Apprendre les pods en tant que _Sum of Square Errors_ (SSE) entre les sorties et les vraies classes
  - Fonction de coûts à minimiser
- Régression linéaire

## One-Vs-All
- Technique pour étendre le Perceptron (ou autre modèle) aux problèmes multi-classes
- Stratégie implémenter dans scikit-learn
- L'idée est que pour chaque classe, on va transformer ça en problème de classification binaire
  - Tout instance qui n'est pas la classe actuelle est considérée comme une classe négative
- Une neurone par classe
  - Nombre de modèles est égale aux nombres de classes
  - Passes un nouvel exemple dans tous les classeurs de façon à trouver celui qui se déclenche
- En général, on préfère avoir une sortie en termes de niveau de confiance où l'on cherche le max
  - Difficile avec des données mal balancées
  - Difficile de s'assurer que la gamme de niveaux de confiance ne varie pas trop d'une classeur à l'autre
- Difficulté est qu'on a toujours beaucoup plus de données négative étant donner que c'est tout contre un

## One-Vs-One
- Stratégie pour étendre le Perceptron (ou autre modèle) aux problèmes multi-classes
- Stratégie populaire dans scikit-learn
- Un classeur par pair de classe
- Vote sur la totalité des classeurs
- Bien expliquer par Scikit-learn : _https://scikit-learn.org/stable/modules/multiclass.html_
- Ne souffre pas du débalancement des données

## Fonction de coûts
- Fonction pour estimer notre erreur
- Clé en ML : Optimisation d'une fonctione objective
  - Souvent _cost_ ou _loss_ function
- Optimiser les paramêtres pour minimiser la fonction de coûts

### Algorithme du Gradient
- Similaire au _Hill Climbing_ (exploration locale)
- Regarde la pente des états voisins
  - Bouger dans la direction la plus abrupte
  - Trouver par la dérivée partielle (diapo 16)
- Peut être en version monter ou décente
- Bénéficie du _feature scaling_
  - Calcul est plus rapide
- Prend beaucoup de mémoire
 
## Hyperparamètres
- Learning rate
  - Learning rate trop haut peut empêcher de converger
  - Learning rate trop faible peut faire tourner l'algorithme longtemps
- Nombre d'epochs
- Il n'y a pas de valeurs parfaites
- Des méthodes existent pour automatiquement calibrer les hyperparamètres

## Stochastic Gradient Descent
- La version de l'agorithme de gradient le plus utilisés
- On y va de manière itérative
- Le faire sur des sous-ensembles de données (batch)
