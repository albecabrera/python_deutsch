# 2. Variante mit logischen Operataren or, and, not

# Spiel beginnen
print("Wir spielen Schere-Stein-Papier")

# Auswahl deklarieren
auswahl_1 = input("Spieler A wählt: ")
auswahl_2 = input("Spieler B wählt: ")

# if, elif, else Bedingung
if auswahl_1 == auswahl_2:
    print("Unentschieden. Beide haben " + auswahl_1 + "-")
elif (auswahl_1 == "Schere" and auswahl_2 == "Papier") or \
     (auswahl_1 == "Stein" and auswahl_2 == "Schere") or \
     (auswahl_1 == "Papier" and auswahl_2 == "Stein"):
    print("Spieler A gewinnt. " + auswahl_1 + " schlägt " + auswahl_2 + ".")
else:
    print("Spieler B gewinnt. " + auswahl_2 + " schlägt " + auswahl_1 + ".")

