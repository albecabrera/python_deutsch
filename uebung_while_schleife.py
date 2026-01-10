einkaufsliste = ["Tomaten", "Milch", "Klopapier", "Brot", "Apfel"]
warenkorb = []

for artikel in einkaufsliste:
    eingabe = input(f"{artikel} in den Warenkorb legen? (ja/nein): ")
    if eingabe.lower() == "ja":
        warenkorb.append(artikel)

print("\nFolgende Artikel hast du in den Warenkorb gelegt:")
print(warenkorb)