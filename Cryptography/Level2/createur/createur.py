#!/usr/bin/env python2.7
from itertools import cycle

# Fonction XOR
def xor(c, k):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(c, cycle(k)))

# Cle utilisee pour l'encryption
key = "StR0nG_K3y"

# Ouvre l'executable, le xor puis l'ecris dans un nouveau fichier
f = open("run", "r")
open("challenge.bin.enc", "w").write(xor(f.read(), key))
f.close()
