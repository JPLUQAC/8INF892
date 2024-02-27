# Cours 8 - 27 février 2024
- Travail 4 sur le _word embedding_
  - Il a un tutoriel
  - Quelques lignes mais doit bien y penser
- **Trouver un sujet de projet avant jeudi le 29**
- Travail d'autoformation 1 et 2 bien réussi en générale
- Pas de cours au retour de la mi-session
  - Période pour travailler sur le projet de session 

# Difficultés des RNN
- Dépendance à long terme
- Dissipation de gradient
  - Si la séquence est suffisament longue, on va perdre le début

## Architectures particulières
- Un RNN classique n'a qu'une couche
- Contrôles des portes

### Long short-term memory (LSTM)
- Introduction d'un mécanisme de portes
- Ajout d'une cellule mémoire
- Porte entré
- Porte sortie
- Porte oublie
- Penser unidirectionnel et bidirectionnel
  - Dépend du cas d'utilisation

# Autoencodeur
- Fameux problème de "curse of dimensionality"
  - Nombre d'échantillons nécessaires augmente de manière exponentielle avec le nombre de dimensions
- Il exsite plusieurs méthodes pour réduire le nombre de dimensions (feature selection)
   - PCA : Principal componenet analysis = tente de modifier la représentation avec moins de dimensions
- Les autoencodeurs font un travail similaire au PCA
- Ils sont conçus et entraîner pour encoder une entrée sous une façon compressé
- Ils sont:
  - Spécifiques aux données
  - Avec pertes
  - Entraînés automatiquement
- Réseau de neurones à 3 couches ou plus
- Fonctionne avec une fonction de perte
  - et optimiseur (stochastic gradient descent)
- Pas très bon pour compresser mais excellent pour généraliser

## Applications
- Débruitage des données
- Réduction de dimensionalité
- Features extractions

## Deep autoencoder
- Nous pouvons facilement modifier les autoencodeurs pour des architectures profondes
- Convolution inversée = Convolution transposé

## Débruitage

## Variational Autoencodeur (VAE)
- Peut décrire une représentation latente en termes probabilistes
  - Plutôt que des valeurs discrètes, nous aurons une distribution de probabilité pour chaque attribut latent
- Cela fait en sorte qu'il peut générer un nombre infinie de versions
- Concept de encodeur et décodeur
- Apprend tranquillement à générer des choses similaires mais différents à ce qu'il a vu
- Moyenne et variance pour la distributions des variables latentes
