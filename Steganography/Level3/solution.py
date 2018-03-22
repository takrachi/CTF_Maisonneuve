#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Ouverture du l'image
im = Image.open('Fire_and_Blood.png', 'r')
# Pixel de l'image
pixel = im.load()
# Dimensions de l'image
w, h = im.size

secret = ""

# Parcourt chacun des pixels de l'image
for y in range(h):
    for x in range(w):
        # Ajoute au secret la conversion ascii du rouge (RGB) du pixel
        secret += chr(pixel[x,y][0])

# Affiche le secret
print secret
