# Datentypen
x = "Hallo Leandro, wie geht es dir heute denn?"
print(x)

# indexing
y = "Alberto"
print(y[2])
print(y[2-5])
print(y[2:7])
print(y[:5])

satz_laenge = "Wie lange ist dieser Satz?"
print(len(satz_laenge)) # bestimmt die Länge eines Satzes
print("Der String mit der Variable Satzlänge ist", len(satz_laenge), "Zeichen lang")

x = "H" + x[1:]
print(x)
# Übung => Gib so effizient wie möglich zehmal den String Hallo aus.
y = "Hallo, Welt"
print(y * 10)
print("Hallo" * 10)

c = "Hallo Welt"
print(c.upper())
print(c.lower())
print(c.split()) # String in einzelne Wörter spliten
print(c.split(","))
print()

d = "Ich liebe Python Tutorials <3"
print(d)
print(d.find("Python")) # Mit find kann man den Index herausfinden
# Übung => Printe mithilfe von Slicing und der find-Funktion nur die Zeichen Python Tutorials <3.
print(d.index("Python Tutorials"))
print(d[10:])






