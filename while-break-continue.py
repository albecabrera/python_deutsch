# while break-continue
# break keyword
# continue keyword
i = 1
while i <= 10:
    if i == 5:
        i = i + 1
        continue # somit wird die Zahl 5 weggelassen
    print(i)
    i += 1
