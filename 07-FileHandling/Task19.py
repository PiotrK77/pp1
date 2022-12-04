file = open("07-FileHandling/integerFrom1to50.txt", "w")

for i in range(1, 51):
    file.write(f"{i}\n")

file.close()