# Die while-Schleife
passwort = "1234"
eingabe = input("Wie lautet das Passwort? ")

versuche = 1
while eingabe != passwort and versuche < 3:
    print("Falsches Passwort.")
    eingabe = input("Wie lautet das Passwort? ")
    versuche += 1
print("Erfolgreich eingeloggt.")

print("Programm beendet.")

print()
# Eine Schleife mit dem Index
i = 0
while i <= 10:
    print(i)
    i += 1
print("So printet man einen index")
