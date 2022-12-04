def identity_matrix(n):
    array = []
    for i in range(0, n):
        array.append([])
        x = -1
        for j in range(0, n):
            x += 1
            if x == i:
                array[i].append(1)
            else:
                array[i].append(0) 
    return array

def displayArr(array):
    for i in array:
        for j in i:
            print(j, end = " ")
        print()

displayArr(identity_matrix(3))
displayArr(identity_matrix(5))
displayArr(identity_matrix(8))