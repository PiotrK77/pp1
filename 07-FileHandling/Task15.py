file = open('07-FileHandling/numbers.txt', 'r')
n = 0
for lines in file:
    n += 1
    if n < 6:
        print(lines, end = "")
    if n == 6:
        n = 0
        input(end = "")

