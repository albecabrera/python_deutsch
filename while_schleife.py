# While-Schleife
#Es gibt drei Sachen, die sehr wichtig sind für eine While-Schleife
i = 0 # 1. Eine Variable außerhalb der Funktion definieren
while i < 11:
    print(i) # 2. Die Variable muss man in der Bedingung verwenden
    i += 1 # 3. Die Variable innerhalb der Schleife verändern (increment, decrement)
passwort = "1234"
eingabe = input("Wie lautet das Passwort:? ")

versuche = 1
while eingabe != passwort and versuche < 3:
    print("Falsches Passwort")
    versuche += 1
    eingabe = input("Wie lautet das Passwort? ")

if eingabe == passwort:
    print("Du bist richtig eingeloggt!")

print("Programm beendet")

