# Cours 2 - 16 Janvier 2024
- Suite au dernier cours
- **Caractéristiques = features**

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

