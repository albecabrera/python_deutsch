from turtle import *

def quadrat(laenge, fuellfarbe=None):
    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()
        i = 0
        while i < 4:
            forward(laenge)
            left(90)
            i = i + 1

        if fuellfarbe:
            end_fill()

quadrat(100, "red")


def dreieck(laenge, fuellfarbe=None):
    dreieck(200, "green")

# Umpositionieren
left(180)
penup()
forward(200)
pendown()
left(180)

def kreis(laenge, fuellfarbe=None):
    if fuellfarbe:
            color(fuellfarbe)
            begin_fill()
    for i in range(120):
        forward(laenge)
        left(3)
    if fuellfarbe:
        end_fill()

kreis(5, "yellow")




exitonclick()

