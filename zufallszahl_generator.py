# Zufallszahlgenerator
# Spiel inittieren (Magische Zahl)
print("Heute spielen wir 'Magische Zahl'")
print("🔮 MAGISCHE ZAHL 🔮")
print("Denke an eine Zahl zwischen 0 und 100.")
print("Antworte bei jeder Frage mit 'ja' oder 'nein'.\n")

# Die 7 magischen Startzahlen (Binärwerte)
werte = [1, 2, 4, 8, 16, 32, 64]

ergebnis = 0

for wert in werte:
    print(f"Ist deine Zahl in dieser Liste enthalten?\n")

    # Zahlen anzeigen, die dieses Bit enthalten
    zahlen = [i for i in range(0, 101) if i & wert]

    # Schöne Ausgabe (10 Zahlen pro Zeile)
    for i in range(0, len(zahlen), 10):
        print(" ".join(f"{z:3}" for z in zahlen[i:i+10]))

    antwort = input("\nAntwort (ja/nein): ").strip().lower()

    if antwort == "ja":
        ergebnis += wert

    print("-" * 40)

print(f"✨ Deine gedachte Zahl ist: {ergebnis} ✨")