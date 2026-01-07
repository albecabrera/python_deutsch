# Wie lautet dein Vorname:? Max
# Wie lautet dein Nachname:? Mustermann
# Hallo Max Mustermann
# Wie alt bist du? 30
# Wow, noch 70 Jahre, dann bist du 100!

vorname = str(input("Wie lautet dein Vorname:?"))
nachname = str(input("Wie lautet dein Nachname:?"))
print("Hallo", vorname + "" + nachname)
alter = int(input("Wie alt bist du:?"))
altersdifferenz = 100 - alter
print("Wow, noch " + str(altersdifferenz) + " Jahre , dann bist du 100!")


