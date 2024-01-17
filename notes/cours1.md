# Cours 1 - 9 Janvier 2024
- Keven Rice est l'auxilaire du cours!

## Présentation du plan de cours
- Travaux d'autoformation pour 30% de la note
- Présentation d'article pour 10% de la note
- Projet pour 25% de la note
- Examen final pour 35% de la note
- Note de passe fixée à 70%
- **Perte de point pour les fautes de français jusqu'à 20%**
- Semaine #13 présents vraimenet l'état de l'art (architecture avancé)
- **Bien déclarer tout outils d'aide et d'inspiration** pour éviter le plagiat

## Introduction
- Le cours se concentre sur les concepts car le domaine évolue rapidement au niveau technique
  - Les libraires changent beaucoup. Café, Tensorflow, Pytorch
  - Ne vaut pas la peine de devenir un expert dans une librairie car ça change 
- Idéal est de travailler sur les ordinateurs du laboratoire
- Cours pars du début avec l'assomption que les étudiants n'ont pas de base en apprentissage machine
- **Matière lourde**
- Beaucoup de temps passer sur les fondements
- **Un réseau de neurons densement connecté est une fonction d'approximation mathématique universelle**
  - Turing complete
  - Cela veut dire qu'il peut apprendre n'importe quel fonction mathématique
  - En théorie, il peut apprendre n'importe quoi
    - En pratique, la complexité algorithmique rend ça difficile
- Théorie est veille (années 80-90s) mais c'est récent en pratique car nous avions besoin du matérielle
- Pas facile de définir l'intelligence artificielle
  - Mauvais nom pour le domaine. Fait référence à un objectif et non ce qui est fait
- Des fois faut prendre ce qui fonctionne le mieux. Ce qui veut dire qu'un algorithme classique peut mieux fonctionner
  - Kévin lance souvent un random forest pour commencer car ça fonctionne asser bien 90% du temps
- **Recommander d'utiliser plusieurs sources d'explications**
- Mettre en pratique les notions théoriques pour bien comprendre
- Format de beaucoup de petit travaux qui sont faciles à faire (selon Kévin)
- Recommander d'essayer Tensorflow et PyTorch, mais le cours ce contre sur Tensorflow
- Mieux de commencer tranquilement le projet final pour s'assurer de bien comprendre
- Aujourd'hui, le légal, marketing, politique etc. se mêle des modèles et des objectfis (penser Chat-GPT)
- **Considérer prendre un livre dans le top 3 des ouvrages de référence**
  - Le troisième est recommander par Kévin
- On ne voit pas les algorithmes d'apprentissage par renforcement dans ce cours
- Professeur du LIARA

### LIARA
- Avant c'était _knowledge driven_
  - Pas une boîte noire!
  - Limite fondamentale : Problème difficile à exprimer/traduire et ça ne se conserve pas bien dans le temps
- Maintenant c'est _data driven_
- Projets:
  - Portvibplate
  - Radars UWB : Radars à bande ultra-large
    - Veille technologie qui vient d'être minituarisé
  - Ville intelligente : Détection des personnes vulnérables dans la ville à partir de noeuds de capteurs
 
## Mise en contexte sur l'apprentissage automatique
- Apprentissage automatique est une sous-discipline de l'intelligence artificielle
  - Une très grosse sous-discipline
- Vise la généralisation, prêt à faire des sacrifices sur la performance
- Souhaites faire des agents apprenants afin de pallier différentes difficultés
- L'IA se redéfinis continuellement
  - Ça va avec les _vagues_
    - D'après Kévin, la vague courrante est là pour rester

## Types d'apprentissage machine

### En fonction du Feedback
- Supervisé : Fonction qui associe les entrées aux sorties
  - Ressemble à un program informatique UQAC sauf qu'on n'a pas spécifié la méthode (juste entrés et sorties)
- Semi-supervisé : Les données d'apprentissage ont parfois une étiquette, parfois non
  - Apprentissage actif : Par avec un enssemble de données de supervisé et revise le modèle continuellement jusqu'a avoir des un résultat acceptable
  - Apprentissage par groupe : On a une idée de ce qui se trouve dans les données, on a l'étiquette mais manque des informations
    - Plus difficile à expliquer comme approche, se diversifie beaucoup
- Non supervisé : Le modèle extrait des patterns dans les entrées sans direction spécifique
  - Résultat dépendent fortement de l'interprétation de l'humain
- Renforcement : L'agent apprend en fonction de récompenses ou punitions
  - C'est à l'agent de décider quoi en faire!
  - Demande beaucoup d'essai et erreur
  - Souvent vu dans l'industrie du jeux vidéo
 
## Ensembles de données
- Remis au prochain cours

## Processus global du ML
- Remis au prochain cours
