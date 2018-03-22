#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Le flag
secret = "  FLAG_d287f6a5780d3efb7f9025cbc0c77026  " * 5

# Transformation du flag en binaire
secret_bin = ''.join('{0:08b}'.format(ord(x), 'b') for x in secret)

# Dimension de l'image a creer
width = 8
height = len(secret_bin) / 8

# Couleur RGB pour un 0
c0 = (0, 0, 0)
# Couleur RGB pour un 1
c1 = (0, 255, 0)

# Creation de l'image
im = Image.new('RGB', (width, height), color = (0, 0, 0)) # Image est noire pour l'instant
pixel = im.load()

# Ajout des couleurs de l'image par rapport au binaire correspondant
for y in range(height):
    for x in range(width):
        pixel[x,y] = c0 if secret_bin[x + (y*width)] == '0' else c1

# Sauvegarde de l'image
im.save('BiColor.png')

