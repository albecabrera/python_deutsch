# Erstelle einen Einkaufsliste-Manager

# Pseudocode schreiben
"""
1. Liste anzeigen
2. Artikel hinzufügen
3. Artikel entfernen
4. Liste sortieren
5. Liste umkehren
6. Artikel suchen
7. Anzahl der Artikel
8. Programm beenden
"""

# Einfache Listenverwaltung

artikel_liste = []

while True:
    print("\n--- MENÜ ---")
    print("1. Liste anzeigen")
    print("2. Artikel hinzufügen")
    print("3. Artikel entfernen")
    print("4. Liste sortieren")
    print("5. Liste umkehren")
    print("6. Artikel suchen")
    print("7. Anzahl der Artikel")
    print("8. Programm beenden")

    auswahl = input("Wähle eine Option (1-8): ")

    if auswahl == "1":
        if len(artikel_liste) == 0:
            print("Die Liste ist leer.")
        else:
            print("Aktuelle Liste:")
            for artikel in artikel_liste:
                print("-", artikel)

    elif auswahl == "2":
        artikel = input("Artikel hinzufügen: ")
        artikel_liste.append(artikel)
        print(f"'{artikel}' wurde hinzugefügt.")

    elif auswahl == "3":
        artikel = input("Artikel entfernen: ")
        if artikel in artikel_liste:
            artikel_liste.remove(artikel)
            print(f"'{artikel}' wurde entfernt.")
        else:
            print("Artikel nicht gefunden.")

    elif auswahl == "4":
        artikel_liste.sort()
        print("Liste wurde sortiert.")

    elif auswahl == "5":
        artikel_liste.reverse()
        print("Liste wurde umgekehrt.")

    elif auswahl == "6":
        artikel = input("Artikel suchen: ")
        if artikel in artikel_liste:
            print(f"'{artikel}' ist in der Liste enthalten.")
        else:
            print(f"'{artikel}' wurde nicht gefunden.")

    elif auswahl == "7":
        print("Anzahl der Artikel:", len(artikel_liste))

    elif auswahl == "8":
        print("Programm wird beendet. 👋")
        break

    else:
        print("Ungültige Eingabe. Bitte wähle 1–8.")
