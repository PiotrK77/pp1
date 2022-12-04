array = [1, 23, 5, 382, 1, 17, 4, 906]

print("-" * ((5 * len(array)) + 1))
print("|", end = "")
for i in array:
    print(" " * (4 - len(str(i)))+ str(i) + "|", end = "")
print()
print("-" * ((5 * len(array)) + 1))