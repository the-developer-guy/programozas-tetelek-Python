T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]

n = len(T)
average = 0
for i in range(n):
    average += T[i]
average /= n
print(f"A T tömb elemeinek átlaga {average}")
