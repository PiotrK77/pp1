array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

m = 0
for i in range(0, len(array)):
    n = 1
    for j in range(0, len(array[i])):
        array[i][j] = (1 + m) * n
        n += 1
    m += 1

print(array)

for i in range(0, len(array)):
    for j in array[i]:
        print(j, end = " ")
    print()
