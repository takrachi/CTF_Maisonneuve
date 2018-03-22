#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Ouverture du l'image
im = Image.open('cthulhu-propaganda.png', 'r')
# Pixel de l'image
pixel = im.load()
# Dimensions de l'image
w, h = im.size

secret = ""

# Parcourt chacun des pixels de l'image
for y in range(h):
    for x in range(w):
        # Cherche la valeur du LSB du bleu de l'image
        secret += str(pixel[x,y][2] & 1)

# On decode le binaire final puis on imprime a l'ecran le secret
print ''.join(chr(int(secret[i:i+8], 2)) for i in range(0, len(secret), 8))

