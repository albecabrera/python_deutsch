# Dictionaries

einkaufsartikel = [
    "Milch", "Brot", "Käse", "Nudeln", "Kaffee", "Bier"
]

preise = [
    1.19, 2.49, 2.99, 1.89, 2.29, 2.79
]
# Dictionaries sind Sammlungen von "Schlüssel-Wert Paaren" (Key-Value Pairs)

artikelpreise = { "Milch": 1.19, "Brot": 2.49}

print(artikelpreise["Milch"]) # Ausgabe: 1.19

# Leeres Dictionary erstellen
artikelpreise = {}
print(artikelpreise)

# Neues Schlüssel-Wert-Paar eintragen
artikelpreise["Rum"] = 10.20
artikelpreise["Wein"] = 15.20
artikelpreise["Bier"] = 2.30
artikelpreise["Apfelschorle"] = 1.50
print(artikelpreise)

# Bestehenden Wert auslesen
wein_preis = artikelpreise["Wein"]
print(wein_preis)

wein_preis2 = artikelpreise.get("Wein") # alternativ
print("Wein Preis 2: " + str(wein_preis))

# Bestehendes Paar "löschen"
del artikelpreise["Bier"]
print(artikelpreise)

# Bestehendes paar "rausnehmen"
wein_preis = artikelpreise.pop("Wein")
print(wein_preis)
print("Weinpreis: " + str(wein_preis))

# Dictionary leeren
artikelpreise.clear()
print(artikelpreise)

# Dictionary vernichten
del artikelpreise









