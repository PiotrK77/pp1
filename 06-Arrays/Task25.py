import numpy

array = [15, 38, 7, 23, 14]

def occurs(number, array):
    for i in array:
        if i == number:
            return True
    return False

print(occurs(14, array))