

einkaufsartikel = []

preise = [
    1.19, 2.49, 299,
    1.89, 2.29, 2.79
]
eingabe = input("Welcher Artikel ?:")

index = einkaufsartikel.index(eingabe)

preis = preise[index]

print("Dieser Artikel kostet ", str(preis))

