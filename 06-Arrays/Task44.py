def convert(array):
    convertedArr = []
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            convertedArr.append(array[i][j])
    return convertedArr

a1 = [[2, 3], [1, 5]]

print(convert(a1))