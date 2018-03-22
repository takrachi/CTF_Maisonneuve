# Level 2

## Description

Fichier du challenge : `challenge.bin.enc`

Mon fichier executable sous Linux a ete encrypte! Pouvez-vous retrouver son contenu?

## Solution

En ouvrant le fichier on peut retrouver le string "StR0nG_K3y" a plusieurs repetition.

En voyant autant de repetition par moment, on peut deduire que l'operation XOR a ete utilise sur le fichier.

Ca signifie que le fichier contient des nullbytes puisque :  nullbyte ^ key = key

Donc sachant la cle on peut XOR le fichier au complet avec la cle. Puis decouvrir le flag dans le binaire en analysant le fichier ou en l'executant .... hehe


**Voir solution.py**

## Creation

**Voir createur/createur.py**

## Flag

FLAG_c2a8ebd5f2d48ab18bf3519316d0b489
