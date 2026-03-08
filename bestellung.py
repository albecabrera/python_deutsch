class Bestellung:
    def __init__(self, artikel, preis):
        self.artikel = artikel
        self.preis = preis

class Kunde:
    def __init__(self, name, bestellung):
        self.name = name
        self.bestellung = bestellung
kunden = [
    Kunde("Anna", [Bestellung("Buch", 15), Bestellung("Stift", 2)]),
    Kunde("Ben", [Bestellung("Laptop", 1000), Bestellung("Laptop", 800)])]

gesamtpreise = []
for k in kunden:
    preise = []
    for b in k.bestellung:
        preis = b.preis
        preise.append(preis)
    gesamtpreis = sum(preise)
    gesamtpreise.append(gesamtpreis)
print(gesamtpreise)


gesamtpreise = [sum(b.preis for b in k.bestellung) for k in kunden]


print(gesamtpreise)
