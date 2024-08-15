T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]
n = len(T)
A = 12

i = 0
while i < n and T[i] != A:
    i += 1
if i < n:
    print(i)
else:
    print("Nincs ilyen elem!")


A = -1

i = 0
while i < n and T[i] != A:
    i += 1
if i < n:
    print(i)
else:
    print("Nincs ilyen elem!")
