# -*- coding: utf-8 -*-
# Datenkapselung

"""
Das Problem ohne Datenkapselung
"""

class Batterie:
    def __init__(self):
        self.ladezustand = 100 # in Prozent

        def entladen(self, prozent):
            self.ladezustand -= prozent

        def __str__(self):
            return f"Batterie: (ladezustand: {self.ladezustand}%)"

b1 = Batterie()
print(b1)
b1.ladezustand = 5000
print(b1)