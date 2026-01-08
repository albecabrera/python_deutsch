# Logische Operatoren and, ort, not
# bei and => es müssen alle Aussagen übereinstimmen, ansonsten wird das Programm beendet.
antwort1 = input("Scheint die Sonne? ")
antwort2 = input("Regnet es? ")
antwort3 = input("Hast du Zeit? ")

if antwort1 == "ja" and antwort2 == "nein" and antwort3 == "ja":
    print("Super, wir gehen spazieren")

# bei or => reicht es alleine, wenn eine der Optionen True ist.
if antwort1 == "ja" or antwort2 == "nein" and antwort3 == "ja":
    print("Super, wir gehen spazieren")

