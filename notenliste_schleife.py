# Listen & while-schleife

notenliste = []

aktiv = True

while aktiv:
    print("Noten: ", notenliste)
    note = input("Note hinzufügen (oder exit): ")

    if note == "exit":
        aktiv = False
    else:
        note = float(note)
        notenliste.append(note)

print("Berechne Notendurchschnitt...")
print()

summe = 0
anzahl_noten = len(notenliste)

i = 0
while i < anzahl_noten:
    note = notenliste[i]
    summe += note
    i += 1

durchschnitt = summe / anzahl_noten
print("Dein Notendurchschnitt: ", durchschnitt)


