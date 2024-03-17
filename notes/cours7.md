# Cours 7 - 20 Février 2024

# CNN
- Terminer les CNNs du dernier cours

## LeNet
- Réseau CNN classique
- Simple
- Downsampling
- Sorties entièrement conectées
- Backpropagation

## AlexNET
- Similaire à LeNet
- Unité d'activation ReLU
- 8 couches
  - 5 conv
  - 3 connectées
- Augmentation de données
  - Transformation avec étiquette
  - Réduction du surapprentissage

## VGG  
- Architecture simple mais très profond pour l'époque
- Convolutions 3x3
- 5 couches de MaxPooling
- 3 couches connectées
- 2-3 semaines d'entraînement sur 4 GPU !
- Demeure un gros modèle aujourd'hui
  - Modèle lourd

## GoogleNet / Inception
- Inuition :
  - Multiples branches
  - Représentation locale
  - Réduction de dimensions
  - Plusieurs templates
- Beaucoup de variants
- Disponbile sur Tensorflow (v3+)
- Classeur auxiliaire
  - Que pour l'apprentissage
  - Pour faire de la rétro propagation
  - Permet de ne pas perdre le gradient

## ResNet - 3.57%
- Modèle complexe mais rapide à l'entraînement
- Fonctionne similairement aux méthodes par ensembles
- Jusqu'à 152 couches pour VI
- Lien résiduel permet de ne jamais perdre notre gradient dans les couches profondes

## Améliorations diverses
- Data augmentation (transformation d'image, par exemple)
- Parallélisations : GPU, Tensor Processing Unit (Google ASIC), etc.

# NLP
- Pas mal remplacé aujourd'hui par les LLMs
- On ne va pas mettre beaucoup de temps sur les NLP
- Le traitement du langauge naturel est une branche de l'IA qui occupe une place considérable
- En ML il s'agit de :
  - Nettoyer et préparer les données
  - Construire une représentation viable des textes pour le ML
  - Entraîner un modèle afin de classer les textes
  - Travailler avec de large texte
- On l'utilise pour :
  - Classification de texte
  - Traduction automatique
  - Correction automatique
  - Description images/sons/etc.
  - Chatbots

## Nettoyage du texte
- moins en moins nécessaire en ML dû aux réseaux de neurones
- Principales tâches classiques :
  - Retrait des marquers et symboles avec le stemming
  - Retour à la forme racine des mots par lemmatisation
  - Retrait des mots vides
- Librairies communes pour les opérations de NLP :
  - NLTK - simple et très complet
  - Gensim - Topic modeling (recherche de sujets)
  - spaCy - Grands ensembles de textes

## Bag of words
- Convertir les données textuelles ou catégoriques en termes numériques
- Permet la conversion de texte en vecteurs de caractéristiques
  - Création d'un vocabulaire de jetons uniques à partir de l'ensemble des documents
  - Construction d'un vecteur qui compte le nombre d'occurrences de chacun des jetons 
- Les vecteurs sont principalement constitués de zéros
- La majorité des mots uniques dans cahq  ue document représentent un petit sous-ensemble du bag-of-words
- Les valeurs des vecteurs sont appelées _raw term frequencies_ : Nombre de fois où un terme _t_ apparait dans un document _d_
- Ce type de séquence est aussi appelée un _l-gram_ ou _unigram_
- En générale on appelle un séquence de mots un _n-gram_
- Le choix de _n_ dépend de l'application et souvent on choisit plus d'un _n_
- Facile à entraîner

### Fréquence des termes
- La fréquence pure des termes n'est souvent pas très utile
- La pertinence n'augmente pas proportionnellement avec la fréquence brute
- Dans les documents beaucoup de mots ne contribuent pas (ou peu) au contenu

### Pondération avec TF-IDF
- On peut réduire l'importance des termes à l'aide de la technique "Term frequency-inverse document frequencey"
- Il faut normaliser par rapport aux autres termes
- Il existe de nombreuses déclinaisons de TF-IDF

### Représentation One-Hot
- La représentation bag-of-words a le défaut de ne pas prendre en compte l'ordre des mots
- On peut aussi utiliser l'encodage one-hot
- Méthode d'implémentation la plus simple
- Pas de fréquence prise en considération
- L'encodage est énorme (taille du dictionnaire pour chaque mot)
- On parle souvent de one-hot vectorization lorsque l'ordre n'est pas préservé
  - Autrement on ne peut passer une matrice one-hot x temps pour préserver

 ### Encodage par index
 - Façon simple d'encoder du texte et de préserver l'ordre
 - Donne un index ou identifiant numérique unique à chaque mot
 - Le texte est une séquence de ces indexes
 - Introduit une distance entre les mots qui n'a pas lieu d'être

 ## Word embedding
 - On peut le voir comme l'ancètre des LLMs
 - Une représentation apprise (ML)
 - En général on peut simplement utiliser un word embedding déjà entraîné
 - Peut être entraîner sans supervision via l'apprentissage par renforcement
 - Chaque mot est représenté par un vecteur de nombre réel
 - Plusieurs méthodes : NN, probabilites, dimensionality reduction
 - Deux grandes approches qui sont un peu à l'opposé

### Skip-gram
- Une des premières approches
- Fenêtre glisasnt sur le texte avec centre=y (target)
- Le hidden-layer est le word embedding

# RNN - Recurrent neural network
- Permet de facilement générer du texte
- Début en 1980
- Famille de réseaux de neurones qui sert aux données séquentielles
- Les modules transformer fonctionne mieux aujourd'hui alors ils ont perdus beaucoup d'importance
- Essaie d'extraire les motifs dans le temps (sur la durée d'une séquence)
- Très flexible au niveau de la forme
  - Beaucoup de tâches variées
- Partage de paramètres à travers différentes parties du modèle (comme les CNN)
- Traite une séquence contenant des vecteurs
- En pratique, il fonctionne en minibatch

## Récurrence
- Toute fonction récurrente peut être considérée comme un RNN
- Les architectures typiques de RNN vont par la suite ajouter des couches supplémentaires à la fin pour lire l'information des états **h** afin de faire des prédictions
- Voir slides pour équations
- Deux avantages majeurs pour le déroulement d'un RNN :
  - Peu importe la longueur de la séquence, le modèle apprit possède toujours la même taille d'entrée
  - Il est possbile d'utiliser la même fonction de transition avec les mêmes paramètres à chaque pas
- Un RNN est en général un réseau qui applique une fonction à une séquence d'entrée
- Les paramètres sont propagés dans le temps (ou dans la séquence)

## Entraînement

### Séquence cible
- On utilise le calcul de l'erreur globale
- Somme de l'erreur dans le temps par rapports aux cibles
- L'erreur peut être calculée de plusieurs façons
- Nous l'utilisons pour effectuer la _backpropagation_

## Applications de RNN
- Reconnaissance du genre musical (MILA)
- Machine Translation
- Image caption
  - Ou l'inverse : trouver une iamge à partir d'une phrase
