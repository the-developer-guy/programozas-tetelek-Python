T = [55, 35, 71, 25, 33, 47]

for i in range(len(T), 1, -1):
    print(i)
    for j in range(i-1):
        if T[j] > T[j+1]:
            T[j], T[j+1] = T[j+1], T[j]

print(T)
