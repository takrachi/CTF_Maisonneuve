#!/usr/bin/env python2
# -*- coding: utf8 -*-
from PIL import Image

# Le flag, on le repete plusieurs fois pour remplir l'image
secret = "On cherche pour le LSB, mais Cthulhu est le MSB.       FLAG_c85bc9ea5038dedcc89c0c3dccac251c          " * 940

# Transformation du flag en binaire
secret_bin = ''.join('{0:08b}'.format(ord(x), 'b') for x in secret)

# Ouverture de l'image (template)
im = Image.open('template.png', 'r')
pixel = im.load()
w, h = im.size

# Modification du LSB des premiers pixels de l'image pour y cacher le message secret.
# Seulement les LSB des valeurs BLEU du RGB seront modifies.
for i in xrange(len(secret_bin)):
    oldp = pixel[int(i%w), int(i/w)]
    pixel[int(i%w), int(i/w)]= (oldp[0], oldp[1], ((oldp[2] & ~1) | int(secret_bin[i])))

# Sauvegarde de l'image
im.save('cthulhu-propaganda.png')

