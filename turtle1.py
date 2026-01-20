from itertools import repeat
from turtle import *

# Code vereinfachen
def quadrat(laenge, fuellfarbe):
    color(fuellfarbe) # Bestimmen der Farbe
    begin_fill() # beginnt zu füllen
    i = 0
    while i < 4:
        fd(laenge)
        rt(90)
        i = i + 1
    end_fill() # Ende des füllens

quadrat(100, "red")

# Umpositionieren
lt(180)
penup()
fd(200)
pendown()
left(180)

# QUADRAT Funktion abrufen
quadrat(80, "blue")


exitonclick() # vermeidet, dass das Fenster ausgeblendet wird.