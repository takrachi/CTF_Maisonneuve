# Level 2

## Description

Fichier du challenge : `BiColor.png`

L'image qui est de dimension 8 x 205 nous donne un indice que c'est des bytes. L'image contient seulement 2 couleurs. 2 couleurs ... 8 pixels par rangee ...

## Solution

Il y a seulement 2 couleurs dans l'image puis une de ces couleurs correspond a un 0 binaire puis l'autre a un 1 binaire. Chacune des rangees de pixel de l'image correspond a 8 bits donc un caractere.

Il suffit de lire les pixels de l'image puis de decoder chaque couleur de pixel pour le bit correspondant puis en decodant la chaine binaire on peut retrouver le message secret.

Un pixel noir equivaut a un 0 binaire puis un pixel vert a un 1.

**Voir le fichier solution.py pour la solution.**

## Creation

**Voir createur.py pour la creation du challenge. **

## Flag

FLAG_d287f6a5780d3efb7f9025cbc0c77026

