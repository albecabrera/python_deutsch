print("🎮 ZAHLEN-RATE-SPIEL 🎮")
print("=" * 40)

# SCHRITT 1: Spielregeln erklären
print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht!")
print("Kannst du sie erraten?")
print()

# SCHRITT 2: Computer wählt geheime Zahl
geheime_zahl = 7

# SCHRITT 3: Spieler gibt Tipp ein
tipp = input("Dein Tipp: ")

# SCHRITT 4: Tipp in eine Zahl umwandeln
tipp = int(tipp)

# SCHRITT 5: Vergleichen und Rückmeldung geben
print()
if tipp == geheime_zahl:
    print("🎉 RICHTIG! Du hast die Zahl erraten!")
    print("⭐ Du hast gewonnen! ⭐")
else:
    print("❌ Leider falsch!")
    print(f"Die richtige Zahl war: {geheime_zahl}")

# SCHRITT 6: Spiel beenden
print("=" * 40)
print("Danke fürs Spielen! 🎮")