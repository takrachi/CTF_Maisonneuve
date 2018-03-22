#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Ouverture du l'image
im = Image.open('BiColor.png', 'r')
# Pixel de l'image
pixel = im.load()
# Dimensions de l'image
w, h = im.size

secret = ""

# Parcourt chacun des pixels de l'image
for y in range(h):
    for x in range(w):
        # Verifie la valeur du pixel RGB puis on decide si c'est un 1 ou 0 binaire.
        if pixel[x,y] == (0, 0, 0) : secret += "0"
        else: secret += "1"

# On decode le binaire final puis on imprime a l'ecran le secret
print ''.join(chr(int(secret[i:i+8], 2)) for i in range(0, len(secret), 8))

