# Level 3

## Description

Fichier du challenge : `Preuve.pdf`

Ce PDF contient des preuves importantes sur l'implication de Taylor Swift dans l'Église de Cthulhu.

Impossible d'ouvrir ce PDF il est corrompu. Il faudra en apprendre plus sur la lecture d'un PDF pour resoudre ce challenge. Il faudra ouvrir le fichier pdf avec un editeur texte puis realiser comment un PDF fonctionne.

## Solution

**Voir le fichier solution.py pour une solution en python**

Un PDF est construit sous forme d'objets puis chacun de ces objets sont declarer par la ligne `# 0 obj`. 
Si le PDF contient, par exemple, 3 objets alors on retrouvera `1 0 obj` `2 0 obj` et `3 0 obj`.

Dans le fichier du challenge on peut s'apercevoir qu'il y a 13 objets mais ceux-ci sont tous declarer sous la forme `1337 0 obj`. On peut donc comprendre que les declarations des objets sont fausses et le but de ce challenge est de redonner les bons numeros aux objets.
Par contre, les objets doivent etre placer dans la bonne ordre. 

Pour trouver l'ordre des objets ont peut se referer au _Cross Reference Table_ sous le nom de `xref` a la fin du PDF.

```
xref
0 14
0000000000 65535 f 
0000008460 00000 n 
0000000019 00000 n 
0000000326 00000 n 
0000008603 00000 n 
0000000346 00000 n 
0000007552 00000 n 
0000007573 00000 n 
0000007759 00000 n 
0000008142 00000 n 
0000008373 00000 n 
0000008405 00000 n 
0000008702 00000 n 
0000008799 00000 n
```

Cette table contient les objets en ordre croissant et leurs offsets dans le fichier.
Elle contient les offsets des objets en ordre croissant.

Pour une meilleure visualisation : https://labs.appligent.com/pdfblog/pdf_cross_reference_table/

```
xref
0 14
0000000000 65535 f 
0000008460 00000 n  >> OBJET 1
0000000019 00000 n  >> OBJET 2
0000000326 00000 n  >> OBJET 3
0000008603 00000 n  >> ...
0000000346 00000 n 
0000007552 00000 n 
0000007573 00000 n 
0000007759 00000 n 
0000008142 00000 n 
0000008373 00000 n 
0000008405 00000 n  >> ...
0000008702 00000 n  >> OBJET 12
0000008799 00000 n  >> OBJET 13
```

En sachant les offsets ou doivent se retrouver les objets, on peut retrouver le bon numero correspondant a chaque objets dans le PDF

```
Par exemple le premier objet que l'on retrouve dans le fichier est:
	1337 0 obj
	<</Length 3 0 R/Filter/FlateDecode>>
	stream 
	[...]
	endstream
	endobj

Dans la table xref on voit que l'objet avec le plus petit offset est l'objet 2.
```

Une fois que les objets ont leur id valide correspondant a la table xref, le PDF est lisible par les interpreteur et on peut retrouver son contenu.

_D'autres solutions sont aussi possible tel que prendre le stream du PDF (qui contient le contenu du PDF) puis le transferer dans un autre PDF valide_

## Creation

**Voir le dossier createur pour la creation du challenge.**

## Flag

FLAG_4240dc66d3996a61652b
