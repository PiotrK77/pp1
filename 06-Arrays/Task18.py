import numpy

array = [15, 8, 31, 47, 2, 19]

sum = 0
for i in range(0, len(array)):
    sum += array[i]

arithmeticMean = sum / len(array)
print(arithmeticMean)