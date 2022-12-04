def transpose_matrix(m):
    transposedArr = []
    for i in range(0, len(m)):
        transposedArr.append([])
        for j in range(0, len(m)):
            transposedArr[i].append(m[j][i])
    return transposedArr

    

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
m3 = [5, 6, 7, 8]