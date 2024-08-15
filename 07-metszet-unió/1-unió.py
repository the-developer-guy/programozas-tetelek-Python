A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 8, 9, 10]
T = []

for i in range(len(A)):
    T.append(A[i])

for i in range(len(B)):
    if B[i] not in A:
        T.append(B[i])
