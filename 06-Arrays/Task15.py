import numpy

array = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, len(array)):
    array[i][i] = 1

for i in range(0, len(array)):
    for j in array[i]:
        print(j, end = " ")
    print()