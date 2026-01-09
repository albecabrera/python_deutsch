# Erstelle das Spiel Schere-Stein-Papier
# Spiel ankündigen
print("Lasst uns Schere-Stein-Papier spielen.")
# Variablen deklarieren
spieler_a = input("Spieler A wählt: ")
spieler_b = input("Spieler B wählt: ")

# if, elif, else Bedingungen
#1. Schere
if spieler_a == "Schere":
    if spieler_b == "Schere":
        print("Unentschieden. Beide haben Schere")
    elif spieler_b == "Stein":
        print("Spieler B gewinnt. Stein schlägt Schere")
    else:
        print("Spieler A gewinnt. Schere schlägt Papier")
#2. Stein
elif spieler_a == "Stein":
    if spieler_b == "Stein":
        print("Unentschieden. Beide haben Stein")
    elif spieler_b == "Schere":
        print("Spieler A gewinnt. Stein schlägt Schere")
    else:
        print("Spieler B gewinnt. Papier schlägt Stein")

#3. Papier
else:
    if spieler_b == "Papier":
        print("Unentschieden. Beide haben Papier.")
    elif spieler_b == "Stein":
        print("Spieler A gewinnt. Papier schlägt Stein")
    else:
        print("Spieler B gewinnt. Schere schlägt Papier")
