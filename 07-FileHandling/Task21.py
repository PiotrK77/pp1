file = open("07-FileHandling/numbersToPower.txt", "w")

for i in range(1, 11):
    file.write(f"{i}, {i ** 2}, {i ** 3}\n")

file.close()