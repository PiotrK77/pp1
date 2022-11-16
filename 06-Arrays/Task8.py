import numpy

array = [-15, -8, -31, -47, -2, -19]


for i in array:

    if i == array[0]:
        minVal = i
        maxVal = i

    if i >= maxVal:
        maxVal = i
    
    if i <= minVal:
        minVal = i

    else:
        pass

print(minVal, maxVal)
    

    