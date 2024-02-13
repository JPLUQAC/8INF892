# Cours 6 - 13 Février 2024
- Cours sur les CNN
- Pas oublier que _Keras_ = _Tensorflow_

# CNN - Convolutional Neural Network
- Types d'apprentissge profond
- Lors de la reprise des réseaux profonds, le plus grand nombre de couches était rechercher
  - Aujourd'hui les architectures modernes ont pas mal tout le même nombre de couche : optimisation
- Très vieux comme concept

## Couches supérieures

### Pooling
- Une de couche de base des CNNs
- Remplace les sorties à l'aide de statistiques sommaires
- Sert à rendre la représentation peu varialbe à de petits changements dans la couche d'entrées
- Différente variation tel que le _Max Pooling_
- Moins populairew aujourd'hui
  - Augmentation de données manuel remplace 
- Foonction inverse du pooling apporte beaucoup de pertes
- On peut faire du pooling plus globabl
- Le pooling permet d'améliorer nettement la qualité de l'apprentissage
- On peut utiliser le pooling directement sur les sorties des convolutions
- Intéressant pour gérer les entrées de tailles différentes
- _Keras_ offre le _MaxPooling_ et _AveragePooling_

### Dropout
- Ajouter au réseau pour la robustesse
- À aider au déclin du pooling
- On désactive certaines unités de manière aléatoire temporairement
- Augmente la performance
- Prévenir le surapprentissage
- Dans les couches denses, les neurones développent une co-dépendance
- Géneralement 20-50% des unitées cachées sont désactivé de façon aléatoire
  - Peut le faire pour chaque minibatch aussi! 
- La différence majeure avec le bagging est que les modèles ne sont pas indépendants un des autres

### Padding
- Peut sortir de l'aire de la données
- Rare en apprentissage automatique 

### Stride
- Assure des prises de données identiques ce qui veut dire qu'une donnée de bord peut être prises dans deux échantillons

## Propriétés diverses

### Entraînement
- l'entraînement peut se faire de différentes façons, mais il faut une fonction de coûtrs dérivable
- On utilise l'algorithme de backpropagation
- Très souvent nous n'avons pas à entraîner notre CNN de nos jours
  - Il existe déjà des modèles entraîner qui peuvent être fine tuner
  - C'est la partie du classeur dans l'architecture qu'on remplace
  - Doit avoir des features similaires par contre!

### Filtres
- Majorité du temps passé à l'entraînement provient de l'entraînement des noyaux qui constituent les filtres
- C'est ceux-ci qui filtrent l'image et permettent l'extraction de caractéristiques
- On peut:
  - Les apprendre de façon supervisée
  -  Les initialiser de façon aléatoire
  -  Construire manuellement (edge detector, corner detector)
  -  Apprendre de façon non-supervisée (avec du clustering) sur de petits morceaux d'images
 
### Tf.Keras.Initializers
- À voir par nous même

### Sorties en tant que structure
- Propriété intéressante des CNNs est qu'ils peuvent retourner un object structuré en haute dimension
  - Plustôt qu'un étiquette de classe ou une valeur réelle de régression
- Le modèle peut donc directement donner la probabilité d'appartenance de cahque pixel à une classe
- Permet au CNN de dessiner des masques précis qui suivent la forme d'objets particuliers dans une image
- Cette tâche s'appelle la segmentation d'images
  - R-CNN sont les modèles ayant le plus de succès
  - Peuvent être construit directement sur VGG, ResNet, etc.
  - Directement en FCN (voir UNET)
  -  

### Types de données
- Canal unique:
  - Signal audio
  - Audio Fournier
  - Données volumétrique (imagerie médicale par exemple)
- Multiple cannaux:
  - Données d'animation
  - Image en couleurs
  - Vidéo en couleurs  
