#!/usr/bin/env python2
# -*- coding: utf8 -*-

# Ouverture du pdf corrompu
pdf = open('Preuve.pdf', 'r').read()

# Trouver la table xref puis on divise chaque ligne en un array
xref = pdf[pdf.find("xref"):pdf.find("trailer")].splitlines()

# On sait que l'adresse des objets se retrouve a partir de la 3ieme ligne du xref donc on enleve les 2 premiers elements
xref.pop(0) # << enleve la ligne qui contient le "xref"
xref.pop(0)
xref.pop(0)

# On se cree un array des objets et leur position dans le pdf.
# Par exemple le premier element de l'array objects_number contiendra sa position dans le pdf
objects_number = dict(enumerate(int(i.replace(" 00000 n", "")) for i in xref))

# On met en ordre les objets par rapport a leur position dans le fichier (xref)
# On a mainenant un array contenant les objects en ordre qui apparaissent dans le pdf
# ATTENTION les objets commence a 0 dans le array, il faudra incremente chacun. (Les objets de pdf commencent par 1 et non par 0)
objects_number = sorted(objects_number, key=objects_number.get)

# Maintenant on peut modifier chacun des 1337 0 obj par le numero correspondant au bonne objet.
for i in objects_number:
    pdf = pdf.replace("1337 0 obj", "%d 0 obj" % (i+1), 1) # On cherche seulement 1 apparition pour permettre de modifier un objet un a la fois

# On peut reecrire le pdf repare dans un nouveau fichier
open('solved.pdf', 'w').write(pdf)
