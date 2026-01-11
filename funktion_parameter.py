# Funktionsparameter (Eingabewerte)

def berechne_flaeche(breite, hoehe): # Funktionskopf
    flaeche = breite * hoehe # Funktionskörper
    print("Der Flächeninhalt des Rechtecks beträgt: " + str(flaeche))

berechne_flaeche(5, 10) # 5 und 10 sind die Argumente und breite und hoehe sind die Parameter

berechne_flaeche(5, 10)

"""
Zusammenfassumg: Jede Funktion besitzt einen Funktionskopf, einen Körper, Parameter und Argumente. 
"""

def backen(temperatur, dauer):
    print("Backe " + str(temperatur) + " temperatur " + str(dauer) + " Minuten.")
backen(180, 15)

