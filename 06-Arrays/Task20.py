import numpy

array = [12, 6, 4, 9, 10]

def star(n):
    for i in range(0, len(n)):
        print(n[i], end = ": ")
        print(n[i] * "*")

star(array)