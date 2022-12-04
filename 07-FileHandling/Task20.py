import random

file = open("07-FileHandling/randomIntegers.txt", "w")

for i in range(0, 50):
    file.write(f"{random.randint(100, 999)}\n")

file.close()