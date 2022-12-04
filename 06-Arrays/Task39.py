array = [[-38, 19], [5,40],[-7,11],[29,16]]

largestValue = []
smallestValue = []

for i in range(0, len(array) - 1):
    for j in range(0, len(array[i])):
        if len(largestValue) == 0:
            largestValue.append(array[i][j])
            largestValue.append(i + 1)
            largestValue.append(j + 1)
        if len(smallestValue) == 0:
            smallestValue.append(array[i][j])
            smallestValue.append(i + 1)
            smallestValue.append(j + 1)
        if array[i][j] > largestValue[0]:
            largestValue[0], largestValue[1], largestValue[2] = array[i][j], i + 1, j + 1
        if array[i][j] < smallestValue[0]:
            smallestValue[0], smallestValue[1], smallestValue[2] = array[i][j], i + 1, j + 1

print(largestValue)
print(smallestValue)