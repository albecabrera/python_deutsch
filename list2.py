# Listen

warenkorb = ["Tomate", "Milch", "Klopapier", "Brot", "Wurst"]  # Eine Liste benötigt immer eckigen Klammern.
# Listenelement hinzufügen

# Auf einzelnes Listenelement zugreifen
print(warenkorb)
print(warenkorb[0])
print(warenkorb[3])

list()
print(list) # mit diesem Befehl ruft man eine Lista auf. s.u

# Ein Element am Anfang der Liste hinzufügen
warenkorb.insert(0, "Bier")
print(warenkorb)

# Bestehendes Listenelemente entfernen / löschen
warenkorb.remove("Tomate")
print(warenkorb)

# Das letzte Element der Liste entfernen
warenkorb.pop()
print(warenkorb)

# Ein Element aus der Liste entfernen
del warenkorb[0] # Bier wird gelöscht
print(warenkorb)#

warenkorb.remove("Milch") # Ein Element entfernen innerhalb einer Liste.
print(warenkorb)



