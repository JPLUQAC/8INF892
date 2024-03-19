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
- 
