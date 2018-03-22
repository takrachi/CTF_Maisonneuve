# Level 4

## Description
LSB Steganography. Un classique mais quand meme difficile. Un message a ete cache dans les _Least Significant Bit_ de ce PNG.

Fichier du challenge : `cthulhu-propaganda.png`


## Solution

Le message est seulement dans les LSB du bleu (RGB) des pixels. 

**Voir le fichier solution.py pour la solution.**

La technique du LSB et de modifier le dernier bit d'une des couleurs du pixel. 
Par exemple, si on veut cacher 1001 dans l'image on modifie les 4 premiers pixels pi on donne comme valeur aux dernier bit de chacun des pixel le bit que l'on veut cacher.

Le principe est que si on modifie le Least Significant Bit d'un pixel, la difference ne se voit a peine sur l'image. 

Exemple si les 4 premiers pixels RGB ont comme valeur
(R, G, B)
(00000000, 00000000, 10101010)
(00000000, 00000000, 10101010)
(00000000, 00000000, 10101010)
(00000000, 00000000, 10101010)

Et on veut cacher 1001. Les pixels deviendront

(00000000, 00000000, 1010101**1**)
(00000000, 00000000, 1010101**0**)
(00000000, 00000000, 1010101**0**)
(00000000, 00000000, 1010101**1**)

Il est aussi possible de remarquer que les derniers bits de la valeur BLEU des pixels contiennent des bit etranges avec un outil tel que Stegsolve.jar.

**Pour une solution avec Stegsolve.jar voir le document solution.pdf**


## Creation

**Voir createur/createur.py pour la creation du challenge.**

## Flag

FLAG_c85bc9ea5038dedcc89c0c3dccac251c

