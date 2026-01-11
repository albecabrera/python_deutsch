# Funktionen mit Rückgabewert

def jahre_in_tage_umrechnen(anzahl_jahre):
    tage = anzahl_jahre * 365
    return tage

def tage_in_stunden_umrechnen(anzahl_tage):
    stunden = anzahl_tage * 24
    return stunden

def stunden_in_minuten_umrechnen(anzahl_stunden):
    minuten =  anzahl_stunden * 60
    return minuten

def minuten_in_sekunden_umrechnen(anzahl_minuten):
    sekunden = anzahl_minuten * 60
    return sekunden

days = jahre_in_tage_umrechnen(1)
hours = tage_in_stunden_umrechnen(days)
minutes = stunden_in_minuten_umrechnen(hours)
seconds = minuten_in_sekunden_umrechnen(minutes)

print("Tage: " + str(days))
print("Stunden: " + str(hours))
print("Minuten " + str(minutes))
print(("Sekunden " + str(seconds)))
