import random

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def rand_elem(array):
    return(array[random.randint(0, len(array) - 1)])

print(rand_elem(array))
