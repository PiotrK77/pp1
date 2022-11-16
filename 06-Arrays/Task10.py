import numpy

array = [1, 3, 5, 7, 9, 2, 1222]

n = len(array)

even = 0

odd = 0


while n > 0:


    if array[n - 1] % 2 == 0:
        even += 1
        n -= 1

    else:
        odd += 1
        n -= 1

print(even, odd)
