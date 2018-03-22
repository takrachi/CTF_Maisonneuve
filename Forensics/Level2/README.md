# Level 2

## Description

Fichier du challenge : `challenge.tar.gz`

Le fichier d'archive tar contient un `app.py` puis une classe compile `Secret.pyc` en python. Nous n'avons donc pas acces au code source direct de la classe Secret, mais le app.py est toujours executable. En executant app.py on voit que la classe Secret contient le _code secret_ mais pour l'obtenir il faut attendre trees...trrrrreeeees longtemps.

## Solution

Plusieurs solutions ici, on peut redefinir la fonction sleep() de python pour eviter l'attente. 

Il est aussi possible de decompiler la classe Secret.pyc. https://github.com/gstarnberger/uncompyle uncompyle le permet. 

Une fois decompile, il suffit d'enlever le sleep() du code ou seulement executer la fonction qui genere le _code secret_

## Creation

**Voir le dossier createur qui contient le code source de Secret.py**

Pour le challenge il faut rouler le code app.py une fois puis supprimer le Secret.py puis donner seulement acces a `app.py` puis `Secret.pyc`

## Flag

FLAG_14066fabe80a7fe8ecb63656daad3c41
