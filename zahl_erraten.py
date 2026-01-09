"""Übungsaufgabe Nr. 3 - Zahl erraten
Bonusaufgabe: Wieviele Versuche hast du gebrauchst (bitte eingeben)
"""

from random import randint
geheime_zahl = randint(1, 100)
print("Ich denke an eine Zahl von 1-100. Errate sie!")

ratespiel = True
versuche = 0

while ratespiel:
    zahl = int(input("Welche Zahl ist es: "))
    versuche += 1

    if zahl > geheime_zahl:
        print("Kleiner")
    elif zahl < geheime_zahl:
        print("Großer")
    else:
        print("Die Zahl ist nun: " + str(geheime_zahl) + "." )
        ratespiel = False
print("Du hast " + str(versuche) + " Versuche gebraucht.")

