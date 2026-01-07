# Datenumwandlung mit float
sparziel = float(input("Was ist dein Sparziel?"))
aktuell = float(input("Wie viel hast du schon?"))

fortschritt = aktuell / sparziel * 100
print("Du hast " + str(fortschritt) + "% deines Sparziels erreicht")