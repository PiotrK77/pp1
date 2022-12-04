import numpy

array = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []
amount = 0


for i in array:
    amount = 0
    for j in array:
        if j == i:
            amount += 1
    if amount == 1:
        unique.append(i)

print(unique)
