import numpy

array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

evenNumbers = 0

for i in range(0, len(array)):
    for i in array[i]:
        if i == 0:
            pass
        elif i % 2 == 0:
            evenNumbers += 1


print(evenNumbers)