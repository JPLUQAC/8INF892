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
- GAN réussissent ces exploits en traînant deux réseaux en compétition coopérative
  - Générateur: Vise à apprendre à générer des fausses données pour tromper le discriminateur
  - Discriminateur: Tente d'apprendre à détecter les fausses données
- Faut trouver un boin compromis dans l'entraînement
  - Générateur ou discriminateur peut s'entraîner trop vite vs l'autre
  - Besoin d'une compétition saine entre les deux pour que les deux apprenents
- Les GAN sont très difficiles à entraîner
- Les GANS souffrent aussi du problème d'effondrement
  - Générateur produit des sorties presque similaires pour différents encodages latents    
