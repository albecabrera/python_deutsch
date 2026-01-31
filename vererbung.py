# -*- coding: utf-8 -*-
"""
OOP - Vererbung
"""
class Tier:
    def __init__(self, name, rasse):
        self.name = name
        self.rasse = rasse

    def geräusch_machen(self, geräusch):
        print(f"{self}: {geräusch}")

    def __str__(self):
        return f"{self.rasse} {self.name}"

t1 = Tier("Doggy", "Schäfferhund")
t1.geräusch_machen("Wuff Wuff...")
t2 = Tier("Hello Kitty", "Munchkinn")
t2.geräusch_machen("Miau Miau...")
t3 = Tier("Oinky", "Jungsau")
t3.geräusch_machen("Grunz Grunz...")




