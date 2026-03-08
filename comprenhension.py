class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# Liste von Personen
personen = [
    Person("Anna", 25),
    Person("Ben", 30),
    Person("Clara", 22),
    Person("David", 35),
    Person("Eva", 20),
    Person("Jens", 50)
]

namenliste = []
for person in personen:
    namenliste.append(person.name)
print(namenliste)

