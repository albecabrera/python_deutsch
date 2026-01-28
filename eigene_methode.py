# Eigene Methode erstellen

class Spieler:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        print("Spieler erstellt:", self.name, self.hp)

    def __str__(self):  # Fehler behoben: Leerzeichen zwischen def und __str__
        return f"Spieler: {self.name} ({self.hp} HP)"  # f-String verwendet

    def angreifen(self, ziel):
        schaden = 20
        ziel.hp -= schaden
        if ziel.hp <= 0:
            ziel.hp = 0
        print(f"{self.name} greift {ziel.name} an und fügt {schaden} Schaden zu!")
    def heilen(self, betrag):
        self.hp += betrag
        if self.hp > 100:
            self.hp = 100
        print(f"{self.name} heilt sich um  {betrag} HP")

# Klassenname mit Großbuchstaben (Spieler statt spieler)
sp1 = Spieler("Darknight5000")
sp2 = Spieler("Darkwarrior5000")

print(sp1)
print(sp2)

# Beispiel für einen Angriff:
sp1.angreifen(sp2)
print(sp2)