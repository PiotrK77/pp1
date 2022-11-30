import numpy

array = [15, 8, 31, 47, 2, 19]

print("existed array:", end = " ")
for i in range(0, len(array)):
    print(array[i], end = " ")
print()

print("reverse array:", end = " ")
for i in range(-1, -len(array) - 1, -1):
    print(array[i], end = " ")
