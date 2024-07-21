T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]

# Eldöntés: benne van-e a 42?
n = len(T)
i = 0
while i < n and T[i] != 42:
    i += 1
if i < n:
    print("A 42 benne van a T tömbben")
else:
    print("A 42 nincs benne a T tömbben")


# Második eldöntés: benne van-e a 34?
n = len(T)
i = 0
while i < n and T[i] != 34:
    i += 1
if i < n:
    print("A 34 benne van a T tömbben")
else:
    print("A 34 nincs benne a T tömbben")
