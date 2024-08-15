A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 8, 9, 10]
T = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            T.append(A[i])
            continue
print(T)

T = []

for i in range(len(A)):
    if A[i] in B:
        T.append(A[i])
print(T)