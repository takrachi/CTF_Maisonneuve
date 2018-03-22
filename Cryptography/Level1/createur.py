#!/usr/bin/env python2
from itertools import cycle

def xor(c, k):  
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(c, cycle(k)))

# secret est le flag, vous pouvez changer ca valeur
secret = "Bravo! J'espere que vous n'avez pas bruteforce la cle ;) Voici votre flag : FLAG_21b7b7aee170e7e290fe7a4061a8eafe"
key = "\x12"

# Creation du challenge
open('challenge.txt', 'w').write("Ce message a ete XOR avec un caractere et encode en hexadecimal : \n%s\n\n" % xor(secret, key).encode('hex'))

