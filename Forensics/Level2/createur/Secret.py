from itertools import cycle
from time import sleep

class Tres_Inutile:
    def __init__(self):
        self.pas_interessant = '\x03\x23\x01\x05\x21'

class Inutile:
    def __init__(self):
        self.part = self.make_part()

    def make_part(self):
        return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip ("Eo@B~2\x1713\x17eBc`\x193B6cD;Fbg\x170\x1543EbBe6B7\x12", cycle(Tres_Inutile().pas_interessant)))

class Secret:
    def get_code(self):
        '''
        Vous ne voulez attendre aussi longtemps, je vous le garantis ;)
        '''
        
        for i in range(2, 12345678, 8):
            print "   [+] sleep(%d)" % i
            sleep(i)
        
        return Inutile().part
