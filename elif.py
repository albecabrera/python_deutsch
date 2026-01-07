# Bedingte Anweisung (elif)

passwort = input("Geben Sie das Passowort ein: ")

geheimes_passwort = "1234"

if passwort == geheimes_passwort:
    print("Erfolgreich eingelogt")
elif passwort == "":
    print("Bitte gebe ein gültiges Passwort ein!")
else:
    print("Passwort falsch!")

print("Programm beendet!")