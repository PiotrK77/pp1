import numpy

array = [15, 8, 31, 47, 2, 19]

n = len(array)

sum = 0

while n > 0:
    sum += array[n - 1]
    n -= 1

arithmeticMean = sum / len(array)
print(arithmeticMean)

