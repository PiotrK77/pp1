import random

def readNumber():
    x = int(input("Enter a number: "))
    return x

def generateNumber():
    return random.randint(1, 9)