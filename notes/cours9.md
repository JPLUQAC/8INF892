# Cours 9 - 19 Mars 2024
- Pas de cours la semaine passé (Kévin était en Chine)

# Deep Recurrent Attentive Writer
- DRAW est techniquement un VAE
  - Vu brièvement
  - Représente une forme naturelle de construction d'image
  - Les parties d'une scène sont créées indépendamment des autres
  - Les croquis approximatifs sont affinées successivement
- Combinaison du variational autoencoder et de deux autres modules particuliers
  - Unités LSTM
  - Module d'attention
- Plutôt que de prendre l'iamge en enter on prend seulement un morceau (à chaque pas de temps)
- Décodeur reprend les principes du VAE
  - Échantiollonne la distribution encodée pour trouver z
- On s'en sert d'entrée pour la seconde couche de LSTM
  - Fonctionne comme nos LSTM précédent
  - Connecte la sortie à une couche dense complètement connectée
  - Activation linéaire

# GAN
- Generative Adversarial Networks

## Introduction
- Type de réseaux de neurones
- Inventés en 2014 par Goodfellow
- Devenus très populaire mais ils sont déjà pu _state of the art_
- Ce sont des réseaux génératifs
  - Ils peuvent créer de nouvelles ndonnées avec un encodage arbitraire, contrairement aux autoencodeurs

## Générations d'images
- Qualité de génération de visages pas possible avec des VAE **simple**
- Modèle de Nvidia en 2017 (Progressive GAN) apporte du photo réaliste

## Principes de base
- GAN réussissent ces exploits en traînant deux réseaux en compétition coopérative
  - Générateur: Vise à apprendre à générer des fausses données pour tromper le discriminateur
  - Discriminateur: Tente d'apprendre à détecter les fausses données
- Faut trouver un boin compromis dans l'entraînement
  - Générateur ou discriminateur peut s'entraîner trop vite vs l'autre
  - Besoin d'une compétition saine entre les deux pour que les deux apprenents
- Les GAN sont très difficiles à entraîner
- Les GANS souffrent aussi du problème d'effondrement
  - Générateur produit des sorties presque similaires pour différents encodages latents
- Bruit gaussien

### Discriminateur
- Deux minibatch de données sont fournies au discriminateur durant l'entraînement
- Pour minimiser la fonction de perte, les paramètres du discriminateur seront mis à jour

### Générateur
- Pour son entraîner, le GAN considère le total des pertes du discriminateur et du générateur comme un jeu à somme nulle
- La fonction de perte est donc le négatif de celle du discriminateur

## Forces
- GAN peut utiliser la backpropagation
- Le générateur ne prend pas les données d'entraînement. Il ne prend que le bruit.
- Auto apprentissage (pas d'étiquette)

## Faiblesses
- Critères d'arrêt peu clairs : Pas de manière objective de dire que le résultat est optimal
- Peut rester emprisonnés dans des optima locaux : Trouve une valeur qui trompe toujours discriminateur dans un cas spécifique alors arrête d'apprendre.
- Presque impossible de retrovuer le bruit qui a générer la donnée
  - XAI...
- Compraison des GAN très subjectif
- Difficle à entraîner

 ## DCGAN
 - Deep Convolutional GAN
 - Pas de pooling
 - Le modèle du discriminateur est pratiquement juste l'inverse du générateur
 - LeakyReLu utilisé dans le discriminateur pour éviter d'avoir des zéros
   - ReLu risque vriament de causé des problèmes
 - S'entraîne bien sur un ordinateur de maison
 - Fausses images générées aléatoirement
   - Aucun contrôle sur les chiffres spécifiques produits
 - Voir code

## Conditional GAN
- CGAN
- On impose une condition aux entrées du générateur et du discriminateur
  - Se présente sous la forme d'une version vectorielle unique du chiffre
- Similaire au DCGAN
