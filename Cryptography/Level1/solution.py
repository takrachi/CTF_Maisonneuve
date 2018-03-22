#!/usr/bin/env python2
from itertools import cycle
from collections import Counter

def xor(c, k):  
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(c, cycle(k)))

#Crack single xored cipher
def crack_single_xor(cipher):
    scoring = "etaoin shrdlu"
    score = 0
    maxScore = [0, 0] #[score, i]

    #Trying every possibilities
    for i in range(256):
        plaintxt = xor(cipher, chr(i))
        mostC = Counter(plaintxt).most_common(5)
        for j in mostC:
            if (ord(j[0]) < 127 and ord(j[0]) > 31):
                if j[0] in scoring or j[0] in scoring.upper():
                    score += 3

        if score > maxScore[0] : maxScore = [score, i]
        score = 0

    return xor(cipher, chr(maxScore[1])), maxScore[0], chr(maxScore[1]) #plaintxt, score, key


f = open('challenge.txt', 'r').read()
cipher = f.split(":")[1].replace("\n", "").replace(" ", "").decode('hex')
plaintext = crack_single_xor(cipher)[0]
print plaintext
