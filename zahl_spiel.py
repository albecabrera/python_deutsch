'''
Erstelle ein Programm, das zwei Spieler nach einer Zahl zwischen 1 und 10 fragt. Das Programm soll dann folgendes ausgeben:

Wenn beide die gleiche Zahl gewählt haben: "Unentschieden! Beide haben [Zahl] gewählt."
Wenn Spieler A eine höhere Zahl hat: "Spieler A gewinnt mit [Zahl] gegen [Zahl]!"
Wenn Spieler B eine höhere Zahl hat: "Spieler B gewinnt mit [Zahl] gegen [Zahl]!"

Hinweise:

Verwende input() für die Eingaben
Denk daran, die Eingabe mit int() in eine Zahl umzuwandeln
Du brauchst if, elif und else Bedingungen
Vergleiche die Zahlen mit ==, > und <
'''
# Spiel initiieren
print("Lasst uns das Zahlenspiel beginnen. Los geht's!")

# Spieler deklarieren
spieler_a = int(input("Welche Zahl hat Spieler A gewählt? "))
spieler_b = int(input("Welche Zahl hat Spieler B gewählt? "))

if spieler_a == spieler_b:
    print("Unentschieden, ihr habt die gleiche Zahl gewählt.")
elif spieler_a > spieler_b:
    print("Spieler A gewinnt mit", spieler_a, "gegen", spieler_b)
else:
    print("Spieler B gewinnt mit", spieler_b, "gegen", spieler_a)