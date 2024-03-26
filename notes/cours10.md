# Cours 10 - 26 Mars 2024
- Premier rapport de sprint ce vendredi
  - Pas grave si on n'a pas beaucoup avancé
- Présentation d'article (travail) sera présenté après la pause 

# Graph Neural Networks
- Contenu avancé
- Vu en surface
- Pas de question avancé sur ce sujet à l'examen
- Grosse branche de recherche
- Matrice d'adjacence

## Historique
- Intérêt en mathématique et informatique depuis très longtemps
- Première application en 1997
- Première référence connu vient en 2005
  - Recurent GNN (RecGNN)
  - Souffrent des mêmes problèmes d'entraînement que les RNN
- Devnus populaires en 2013 avec les ConvGNN
  - Convolution
- Depuis il exite des GNN exploitant tous les types : GAE, Transformeur, etc.

## Motivation
- Information relationnelle capturer par les graphes
- CNN et RNN ne capturent pas bien l'information contextuelle des noeuds
- Se retrouvent naturellement un peu partour autour de nous
  - Réseaux informatiques
  - Événements
  - Propagation de maladies
  - Métro/Train
  - etc.
- Les domaines complexes possèdent une structure relationnelle riche qui peut être représentée par un graphe relationnel
  - Forme 3D
  - Graphe de scène
  - Regulatory Networks (?)

## Types de graphe
- Dirigée (directed)
- Non-dirigée (undirected)
- Pondérée (Weighted)
- Connaissance (Knowledge)

## Tâches possibles
- Prédiction de noeuds
- Générations de graphes
- Prédiction de liens
- Sous-ensembles de graphes

### Alphafold
- Prédiction de noeuds
- Prédire de manière computationnelle la structure 3D d'une protéine uniquement de sa séquence d'acides animées
- Pour chaque noeud, prédire ses coordonnées 3D
- L'idée est d,utilise un graphe spatiale

### Recommandation
- Prédiction de liens
- Utilisateurs interagissent avec des articles
- Noeuds: utilisateurs et articles
- Arêtes: interactions utilisateur-articles
- Objectif : Recommander des articles que le sutilisateurs pourraient aimer
- Utiliser par Netflix, magasin en ligne, etc.

### Intéraction de médicaments
- Prédire les effets secondaires des médicaments dans le contexte d'un patient qui prend plusieurs médicaments
- Noeuds: médicaments et protéines
- Arêtes: interactions

### Traffic
- Prédictions de graphes
- Noeuds: segments de route
- Arêtes: connectivité entre les segments de routes
- Google Maps : DeepMind utilise un approche basée sur les GNN

## Outils populaires
- PyTorch Geometric
  - Expressément pour PyTorch   
- Deep Graph Library
  - Fonctionne avec PyTroch, Tensorflow et Apache MXNet

# Node Embedding
- Connecté les noeuds dans un espace latent
- Similarité entre les embeddings de plusieurs noeuds indique leur similarité dans le réseau
- Cela permet d'encoder automatiquement l'information du réseau
- Peut donc server à différents types de tâches liés aux graphes

## Composants clés
- Besoin d'un Encodeur
  - Nous allons couvrir les encodeurs profonds par la suite avec nos GNN   
- Une fonction de similarité ou une distance
  - Ex: Minkowski

## Méthodes d'encodage
- Les méthodes sans caractéristiques sont dites par proximité
  - Ex: Nous avons juste des étiquettes
  - Trouve les marche aléatoires (Random Walk)
  - Trouve les marches biaisées (Biased Random Walk)
  - Embedding seront indépendants de la tâche, ce que est avantageux pour la généralisation
  - Entraînés par auto-apprentissage ou apprentissage non-supervisé
- Les méthodes basées sur les caractéristiques sont plus classique
  - AE profonds
  - Factorisation matricielle

### Random Walk
- Rétropropagation
- Gradient
- Chance de partir d'un noeud et tomber sur un noeud X
- Direction (examintion des voisions) aléatoires

#### Biased Random Walk
- On ajoute l'échantillonnage
- Biaser la marche aléatoire
- Toutes sortes de stratégies existent
  - Node2Vec

 
