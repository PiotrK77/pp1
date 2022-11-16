import numpy

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Brzeczyszczykiewicz"]

print(max(array, key = len))

for i in array:

    if i == array[0]:
        longestString = i

    if len(i) > len(longestString):
        longestString = i

    else:
        pass

print(longestString)

