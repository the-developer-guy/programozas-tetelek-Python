T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]
A = []
B = []

for i in range(len(T)):
    if T[i] % 2 == 0:
        A.append(T[i])
    else:
        B.append(T[i])
