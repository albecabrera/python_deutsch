# Listen & while-schleife

einkaufsliste = ["Tomaten", "Milch", "Klopapier", "Brot", "Apfel"]

warenkorb = []

i = 0
while i < len(einkaufsliste):
    eingabe = input((einkaufsliste[i]) + " in den Warenkorb legen? (ja/nein)")
    if eingabe == "ja":
        warenkorb.append(einkaufsliste[i])

    i = i + 1

print("Folgende Artikel hast du in den Warenkorb gelegt: ")
print(warenkorb)