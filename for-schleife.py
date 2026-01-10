# for-schleife mit range() und enumarate()
# range => es bleibt immer in einem Rang
zahlenliste = range(1,21,3)

for zahl in zahlenliste:
    print(zahl)

# enumerate
namen = ["Hans", "Anna", "Tom", "Maria"]

for index, name in enumerate(namen): # Somit werden alle Namen aufgezählt. 
    print(str(index+1)+ ". " + name)
