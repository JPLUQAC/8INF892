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
- 
