from time import time

# Traditionelle Schleife

start1 = time()
print(start1)
liste = []
for i in range(1000000):
    liste.append(i * 2)
end1 = time()
dauer1 = end1 - start1
print(f"Schleife: {dauer1:.4f} Sekunden")
