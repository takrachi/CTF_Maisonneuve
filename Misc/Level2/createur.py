#!/usr/bin/env python2
# Lol creation de JS en python don't judge plz

secret = list("FLAG_1f0e02e1800772f146d1b76a79dbcc0c")

chall = "[]" + ''.join("+("+"-~{}"*ord(i)+")+' '" for i in secret)

open('challenge.html', 'w').write(chall)
