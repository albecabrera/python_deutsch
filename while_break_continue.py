# while mit break und continue

i = 0
while i <= 10:
    if i == 5:
        break # break unterbricht die while-schleife
    print(i)
    i += 1

print()
# continue
i = 0
while i <= 10:
    if i == 5:
        i = i + 1
        continue # continue zählt bis 4 und überspringt die 5 1,2,3,4,6,7...
    print(i)
    i += 1
print()

is_runing = True
while is_runing:
    eingabe = input("Möchten Sie abbrechen (exit)")
    if eingabe == "exit":
        is_runing = False
print("Program beendet.")


