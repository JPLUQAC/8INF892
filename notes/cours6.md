# Cours 6 - 13 Février 2024
- Cours sur les CNN

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
- 
