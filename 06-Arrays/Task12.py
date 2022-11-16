import numpy

array = [[2,5,4],[9,0,3]]

print(array)

print(f"array rows: {len(array)}, array columns: {len(array[0])}")

print(array[0][1])

print(array[1][2])

print("")

for i in array[1]:
    print(i, end = " ")

print("\n")

for i in range(0, len(array)):

    for i in array[i]:
        print(i, end = " ")
    
    print("")

for i in range(0, len(array)):
    print(array[i][-1])