A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 8, 9, 10]
T = set()

for number in A:
    T.add(number)
for number in B:
    T.add(number)
print(T)