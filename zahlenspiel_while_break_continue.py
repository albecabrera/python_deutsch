"""Übung: Zahlenspiel mit while, break und continue
Aufgabe:
Schreibe ein Programm, das den Benutzer wiederholt nach Zahlen fragt. Das Programm soll:

Eine Endlosschleife mit while True starten
Den Benutzer nach einer Zahl fragen
Wenn der Benutzer "stop" eingibt, soll die Schleife mit break beendet werden
Wenn die Zahl negativ ist, soll sie übersprungen werden (continue) mit der Meldung "Negative Zahlen werden ignoriert!"
Wenn die Zahl positiv ist, soll sie zur Summe addiert werden
Am Ende soll die Gesamtsumme aller positiven Zahlen ausgegeben werden"""
from operator import contains

print("Zahlenspiel")
summe = 0
while True:
    eingabe = input("Gib eine Zahl ein (oder 'stop' zum Beenden): ")
    if eingabe == "stop":
        break
    zahl = float(eingabe)
    if zahl < 0:
        print("Negative Zahlen werden ignoriert!")
        continue
    summe = summe + zahl
print(f"Die Summe aller positiven Zahlen ist: {summe}")