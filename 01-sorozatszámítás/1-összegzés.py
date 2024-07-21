# Véletlenszám-generátorral előállított 20 pozitív egész szám
T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]
# Az n elemszámot megadhatjuk kézzel is, vagy megkérdezzük a "tömbtől" (ami lista), hány eleme van
# A len() - length függvény adja vissza, hogy egy objektumnak hány eleme van
n = len(T)

sum_value = 0
for i in range(n):
    sum_value += T[i]
print(sum_value)

# Ugyanez Pythonosan, a példa kedvéért
sum_value = 0
for num in T:
    sum_value += num
print(sum_value)

# Erre ráadásul beépített függvény is van!
sum_value = sum(T)
print(sum_value)
# Ezért nem illik sum-nak elnevezni az összeget!
