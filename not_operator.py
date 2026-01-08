# bei not => wird ein nein als True und nicht ja als False interpretiert

antwort1 = input("Scheint die Sonne? ")
if not antwort1 == "nein":   # das bedeutet hier, dass die erwartete Antwort ein Ja/True entspricht...
        print("Wir gehen spazieren")
print("Programm beendet!")