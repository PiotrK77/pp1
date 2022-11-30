import numpy

array = [[True,False],[True,True],[False,False]]

for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        if array[i][j]:
            array[i][j] = False
        else:
            array[i][j] = True
        
print(array)