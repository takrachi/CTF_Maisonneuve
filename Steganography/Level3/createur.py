#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Le flag 
secret = "Red is the color of extremes. It's the color of passionate love, seduction, violence, danger, anger, and adventure. Our prehistoric ancestors saw red as the color of fire and blood              FLAG_0d424ffa6d7f2141f11cff62425ba6a4    "

# On veut une dimension d'image assez grande donc on repete le secret
while len(secret) < 40000: # On veut une image au moins de 200 x 200
    secret *= 2 # Double le secret

# Dimension de l'image a creer
width = 200
height = len(secret) / 200

# Creation de l'image
im = Image.new('RGB', (width, height), color = (0, 0, 0)) # Image est blanche pour l'instant
pixel = im.load()

# Creation des pixels de l'image
for y in range(height):
    for x in range(width):
        # La valeur du rouge dans le RGB du pixel sera le nombre ascii correspondant du secret
        # Le vert et bleu seront seulement noir (0)
        pixel[x,y] = (ord(secret[x + (y*width)]), 0, 0)

# Sauvegarde de l'image
im.save('Fire_and_Blood.png')
