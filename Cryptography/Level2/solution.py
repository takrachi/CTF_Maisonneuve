#!/usr/bin/env python2.7
from itertools import cycle

# Fonction XOR
def xor(c, k):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(c, cycle(k)))

# En ouvrant le fichier on decouvre que la cle est StR0nG_K3y
key = "StR0nG_K3y"

# Ouvrir le fichier puis xorer avec la cle pour retrouver le fichier original
f = open("challenge.bin.enc", "r").read()
open("solution.bin", "w").write(xor(f, key))
