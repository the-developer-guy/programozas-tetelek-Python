T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]

min_value = T[0]
for i in range(1, len(T)):
    if T[i] < min_value:
        min_value = T[i]
print(min_value)
