# Cours 5 - 6 Février 2024
- Dernier 25-30 minutes du cour conservé pour discuter du projet

# Entrapînement

## Fonction de coûts
- Vient mesuré l'erreur dans le réseau
- On utilise sa dérivé pour entraîner le modèle (modifier les poids)
- Voir le code

## Backpropagation (Propagation arrière)
- Algorithme, façon de calculer les gradients
- Algorithme efficace (d'un point de vue algorithmique) qui permet de calculer les dérivées d'une fonction de coûts complexe
  - On utilise les dérivées pour apprendre les pods
- L'intuition derrière l'algorithme de propagation arri`re est de renverser une opération pour réduire les coûtrs en calculs
-  Voir le code
-  **Très important à comprendre**

## Fonctions d'activiation
- Deux familles
  - Linéaires
  - Non-linéaires
- Non-linéaires est beaucoup plus intéressant pour nous car elle s'adapte mieux au réseau complexe
- Fonctions monotones : Toujours ascendent
- Fonction non-monotones : Peut décendre et monter
  - Si trop extrême, l'entraînement devient instalbe. Difficle de converger
  - Peu de fonction d'activitation de ce type : Ex Swish (notions avancées)
-  On va se contrer sur les fonctions monotone

### Sigmoid et Hyperbolic Tangent (TANH)
- Monotone
- Voir slide 7

### Rectified Linear Unit (RELU)
- Dans certains cas, Sigmoid, Tanh, peuvent occasionner des problèmes (apprentissage bloqué)
- C'est une fonction monotone et sa dérivée aussi!
- Moins de problèmes de gradients qui disparaissent dans les réseaux avec beaucoup de couches
- Les opérations sont plus simples (pas d'exponentielle, moins de calculs)
- Beaucoup de valeurs d'unités ReLU sont à zéro ce qui peut accélérer la convergence
- Toutes les valeurs négatives deviennent zéro
- Parfois ce n,est pas souhaitable, cela peut arrête l'entraînement au niveau des entrées négatives
- On peut recitifer avec un Leaky ReLU ou encore une version plus générique Parametric ReLU

#### ReLU et Matrices Creuses
- Les activations tombant souvent à zéro, on dit que ReLU occasion des matrices d'activation creuse (beaucoup de zéros)
  - Gain en vitesse pour le réseau, puisque les calculs sont faciles
  - Mais aussi un gain en espace
    - Enregistre les éléments plutôt que des tabelaux 2D
- _Dead ReLUs problem_ peut devenir non négligeable dans les grands NN (la plupart ne sont plus mis à joir)
- Les ReLU ne corrigent pas l'inverse du _vanishing gradient_
- Ainsi, ils souffrent du _exploding gradient_
  - Moins critique   
