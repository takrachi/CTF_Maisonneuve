# Level 1

## Description

Fichier du challenge : `Trash.jpg`

On soupçonne que ce papier donne le nom de l'opération que la grande prêtresse, Taylor Swift, organise pour take over Hollywood des mains de l'Église de Scientologie! 

Cette image nous a ete donnee par quelqu'un qui voulait rester dans l'anonymat, mais il semble que ce fichier ne contient pas seulement une image ...

## Solution

Il est possible de trouver sur internet que ce texte correspond a du cthulhu text, mais l'image ne contient pas seulement un jpg mais aussi le dictionnaire de traduction de ces symboles. 

Il suffit d'extraire le dictionnaire qui est dans un dossier compresse ZIP.

Pour ce genre de challenge j'aime bien utiliser **binwalk**. binwalk permet de verifier le contenu d'un fichier puis aussi d'extraire ceux-ci. 

`binwalk challenge.png`

On vois que le fichier contient un PNG puis un ZIP

`binwalk -e challenge.png`

Extrait les fichiers du fichier.

Un autre outil efficace est **foremost**. Il analyse et extrait les fichiers d'un fichier.
`foremost challenge.png`

Une fois le ZIP extrait, il suffit de le decompresser.

Puis en decodant les symboles ont decouvre que le nom d'operation est `KillTomCruise`.

## Creation

J'ai cache un fichier compresse ZIP mais il est possible de cacher pas mal n'importe quoi. En fait j'ai juste concatener les deux fichiers dans un. Le premier fichier qui apparait c'est celui qui sera reconnu.

J'ai utilise python pour creer le challenge.
`python2 -c 'open("Trash.jpg", "a").write(open("dictionnaire.zip", "r").read())'`

## Flag

KillTomCruise
