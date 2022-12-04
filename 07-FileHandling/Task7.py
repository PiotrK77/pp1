file = open('07-FileHandling/countries.txt', 'r')
n = 0
for line in file:
    n += 1
    print(f"{n}.", line, end = "")
file.close()