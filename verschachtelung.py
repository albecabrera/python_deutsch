# Verschachtelte begingte Anweisung
# If-Anweisung
kontosand = 1000
passwort = input("Geben Sie das Passwort ein:")
geheimes_passwort = "1234"

if passwort == geheimes_passwort:
    print("Erfolgreich eingeloggt")
    betrag = int(input("Wie viel möchten Sie abheben? "))
    if betrag > kontosand:
        print("Du kannst kein Geld mehr abheben. Achtung, du bist in minus!!! ")
    else:
        kontosand = kontosand - betrag

elif passwort == "":
    print("Bitte gebe ein gültiges Passwort ein:")
else:
    print("Passwort falsch")

print("Sie haben noch " + str(kontosand) + "€ zur Verfügung.")

print("Programm beendet.")



