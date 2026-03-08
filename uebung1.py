'''
Wie lautet dein Vorname? Max
Wie lautet dein Nachname? Mustermann
Hallo, Max Mustermann!
Wie alt bist du? 30
Wow, noch 70 Jahre, dann bist du 100!
'''

vorname = input("Wie lautet dein Vorname? ")
nachname = input("Wie lautet dein Nachname? ")
print(f"Hallo, {vorname} {nachname}!")

alter = int(input("Wie alt bist du? "))
jahre = 100 - alter
print(f"Wow, noch {jahre} Jahre, dann bist du 100!")