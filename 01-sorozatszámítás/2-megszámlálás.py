T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]

# Példa: hány páros elem van?
even_count = 0
for i in range(len(T)):
    if T[i] % 2 == 0:
        even_count += 1
print(f"{even_count} db. páros szám van a T tömbben.")
