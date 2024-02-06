# Cours 5 - 6 Février 2024
- Dernier 25-30 minutes du cour conservé pour discuter du projet

## Backpropagation (Propagation arrière)
- Algorithme, façon de calculer les gradients
- Algorithme efficace (d'un point de vue algorithmique) qui permet de calculer les dérivées d'une fonction de coûts complexe
  - On utilise les dérivées pour apprendre les pods
- L'intuition derrière l'algorithme de propagation arri`re est de renverser une opération pour réduire les coûtrs en calculs
-  Voir le code
-  **Très important à comprendre**

## Fonctions d'activiation
- Deux familles
  - Linéaires
  - Non-linéaires
- Non-linéaires est beaucoup plus intéressant pour nous car elle s'adapte mieux au réseau complexe
- Fonctions monotones : Toujours ascendent
- Fonction non-monotones : Peut décendre et monter
  - Si trop extrême, l'entraînement devient instalbe. Difficle de converger
  - Peu de fonction d'activitation de ce type : Ex Swish (notions avancées)
-  On va se contrer sur les fonctions monotone

### Sigmoid et Hyperbolic Tangent (TANH)
- Monotone
- Voir slide 7

### Rectified Linear Unit (RELU)
- Dans certains cas, Sigmoid, Tanh, peuvent occasionner des problèmes (apprentissage bloqué)
- C'est une fonction monotone et sa dérivée aussi!
- Moins de problèmes de gradients qui disparaissent dans les réseaux avec beaucoup de couches
- Les opérations sont plus simples (pas d'exponentielle, moins de calculs)
- Beaucoup de valeurs d'unités ReLU sont à zéro ce qui peut accélérer la convergence
- Toutes les valeurs négatives deviennent zéro
- Parfois ce n,est pas souhaitable, cela peut arrête l'entraînement au niveau des entrées négatives
- On peut recitifer avec un Leaky ReLU ou encore une version plus générique Parametric ReLU

#### ReLU et Matrices Creuses
- Les activations tombant souvent à zéro, on dit que ReLU occasion des matrices d'activation creuse (beaucoup de zéros)
  - Gain en vitesse pour le réseau, puisque les calculs sont faciles
  - Mais aussi un gain en espace
    - Enregistre les éléments plutôt que des tabelaux 2D
- _Dead ReLUs problem_ peut devenir non négligeable dans les grands NN (la plupart ne sont plus mis à joir)
- Les ReLU ne corrigent pas l'inverse du _vanishing gradient_
- Ainsi, ils souffrent du _exploding gradient_
  - Moins critique   

#### Scaled ELU
- Alpha et gamme sont fixées
  - Ils sont déterminés à partir des entrées
  - Voir l'article original qui a plus de 93 pages d'annexes pour expliquer (haha)
- Utilisés avec une initialisation spécifique des poids, nous obtenons des SNN - Self Normalizing Neurons
- Il est démontré qu'on ne peut pas avoir de _vanishing_ ou _exploding_ gradient
- Les réseaux convergent plus vite
- On doit utiliser _lecun normal_ dans Keras
- Nous verrons plus tard avec le dropout

### Swish
- Dévloppé par Google Brain et basé sur PFLU
- Non monotone, mais visait à détrôner ReLU
- Rapidement beaucoup de **dead ReLU**, nuisible dans les réseaux très prodonfs
- Bornée en négatif, à utiliser avec _batch normalizatrion_

### Softmax
- Softmax se base sur les principes de la fonction d'activation logistique
  - On produit un résultat qui est une probabilité d'appartenance à une classe entre 0 et 1
- Softmax étend cette idée aux problèmes multiclasses
  - La somme des probabilités devient égale à 1
  - Chaque classe vaut entre 0 et 1
- Ne fonctionne pas si vos instances peuvent appartenir à la fois à plusieurs classes
  - On doit retourner vers Sigmoide (la fonction logistique)     

## Fonction de coûts
- Vient mesuré l'erreur dans le réseau
  - Somme des erruers
  - Chaque couche doit avoir une fonction de coûts et chaque fonction de coûts a son propre minimum
  - Fonction mathématique complexe à optimiser
- Concrètement, c'est la dérivée dû calcul de l'erreur qui permet de mette à jour chacun des pods 

### Fonctions simples
- Mean Squared Error (MSE)
- Mean Absolute Error (MAIE

### Cross-Entropy
- NLLL et Cross-Entropy sont des fonctions similaires qui servent pour la clasfication binaire, Keras offre justement juste Cross-Entropy
- Tensorflow offre pas mal de variations de la cross-entropy
  - BinaryCrossentropy : uniquement utilisable pour les problèmes binaires avec étiquettes
  - BinaryFocalCrossentropy : ajoute une fonction pour focaliser sur les exemples difficiles
  - CategoricalCrossentropy : celle qu'on vient de voir avant
  - SparseCategoricalCrossentropy
    - Étiquettes sous la forme d'entiers, non de one-hot
    - La sortie est quand même un vecteur
    - Surtout intéressante pour éviter l'encodage lors de problème avec énormément de classes possibles (NLP)

### Hinge Loss
- Lorsque la distance avec le seuil est moins que 1, la perte vaut 0
- Si le point est sur le seuil, la perte est 1
- Si la distance est négative, la perte augmente linéairement
- Les instances bien classées ont une perte minimal
- Souvent utilisée pour entraîner les SVM
- Elle tente de favoriser les exemples qui sont loin du seuil
- On peut l'utiliser dans TF en autant que nos classes soient entre -1 et 1... supporte aussi 0 à 1 mais les valeurs seront reconverties

### Kullback-Leibler
- Divergence de KL est très populaire en deep-learning, en particulier pour les modèles génératifs que nous verrons plus tard
- En probabilitées, elle permet de mesurer la quantité d'informations perdues en simplifiant une distributioon par une autre visant à l'approximer
- On utilie encore la notion d'entropie
- En somme, le log base 2 s'interprète comme étant le minimum de bits nécessaire à l'encodage de l'information
- Va plus loin que l'en tropie en calculant comment compresser de façon à s'approcher de l'encodage optimal
- KLL n'est pas symétrique et ne peut donc pas servir de distance
- On va revoir plus tard

### Similarité cosinus
- Permet de connaître la similarité cosinus entre -1 et 1 pour deux instances de vecteurs
  - 1 = très similaire
  - 0 = ortogonaux
  - -1 = très différents
- En réalité ça fait peu de sens mais ça nous permet d'introduire son utilié en ML

# Projets
- De notre choix
- Peut être plus scientifique ou plus appliqué
- Doit être en mesure d'expliquer nos décisions
- Perd pas de points si ça ne fonctionne pas
- Langauge de notre choix
  - Valider avec prof si on utilise un language obscure
- Porter une attention particulière aux données
  - Quantité
  - Leurs provenance
  - Qualité
  - etc. 

## Objectifs
- Inégrer différentes notions apprises en cours à l'intérieur d'un projet plus large
- Développer un logiciel de taille moyenne en suivant une méthodologie rigoureuse
- Comprendre la relation entgre la théorie vue en classe et l'implantation réelle
- Comprendre les difficultées liées à la modélisation des données
- Devenir apte à justifier les décision de concept en IA
- Approfondir ses connaissances de mani`res autodidacte
- Acquérir de l'expertise dans le développement d'intelligence artificielle

