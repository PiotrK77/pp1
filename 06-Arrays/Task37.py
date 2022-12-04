def create_2d_arr(x, y):
    array = []
    subsetArray = []
    for j in range(y):
        subsetArray.append(0)
    for i in range(x):
        array.append(subsetArray)
    return array

print(create_2d_arr(3, 5))