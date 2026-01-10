# Membership-Operatoren "in" und "not in"

wichtiger_einkaufsartikel = "Tiefkühlpizza"
einkaufsliste = []

aktiv = True
while aktiv:
    print("Einkaufsliste:", einkaufsliste)
    einkaufsartikel = input("Artikel hinzufügen (oder exit): ")

    if einkaufsartikel == "exit":
        if wichtiger_einkaufsartikel not in einkaufsliste:
            eingabe = input(wichtiger_einkaufsartikel + " noch hinzufügen? (ja/nein): ")
            if eingabe == "ja":
                einkaufsliste.append(wichtiger_einkaufsartikel)
        aktiv = False
    else:
        if einkaufsartikel in einkaufsliste:
            print()
            print("Artikel ist bereits vorhanden.")
            print()
            continue
        einkaufsliste.append(einkaufsartikel)
        print()
        print(einkaufsartikel + " wurde hinzugefügt.")
        print()

print("==================")
print("Einkaufsliste:", einkaufsliste)
print("==================")