T = [55, 35, 71, 25, 33, 47, 12, 77, 32, 86, 95, 83, 83, 38, 47, 54, 11, 60, 21, 34]

# Eldöntés: benne van-e a 42?
found = False
for number in T:
    if number == 42:
        found = True
        break
if found:
    print("Benne van a 42.")
else:
    print("Nincs benne a 42.")
