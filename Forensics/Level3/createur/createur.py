#!/usr/bin/env python2
# -*- coding: utf8 -*-
import re

# Ouverture du PDF non corrompu
pdf = open('template.pdf', 'r').read()

# Remplace tout les objets par 1337
pdf_corrompu = re.sub("\d+ 0 obj", "1337 0 obj", pdf)

# Ecriture du challenge
open('Preuve.pdf', 'w').write(pdf_corrompu)
