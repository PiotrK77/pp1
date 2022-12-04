array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

for i in array:
    for j in i:
        print(j, end = " ")
    print()

print("--------------")

for i in range(0, len(array)):
        array[i][0], array[i][-1] = array[i][-1], array[i][0]

for i in array:
    for j in i:
        print(j, end = " ")
    print()