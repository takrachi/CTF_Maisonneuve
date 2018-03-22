# Level 1

## Description

Fichier du challenge : `challenge.txt`

Voir challenge.txt. Le message a ete XOR avec un caractere seulement, etes-vous capable de retrouver le message?

## Solution

Il est possible de bruteforce le caractere qui a ete utilisee pour XOR vu que c'est seulement 255 possibilites.

La solution que je donne (**solution.py**) contient une methode qui cherche la cle la plus probable avec un module de _score_. Dans le fond je regarde les resultats des XOR et je retiens seulement ceux qui contiennent le plus des caracteres les plus utilisees en anglais/francais.

## Creation

J'ai seulement XOR le flag avec \x12 comme cle (un caractere non lisible). **Voir createur.py**

## Flag

FLAG_21b7b7aee170e7e290fe7a4061a8eafe
