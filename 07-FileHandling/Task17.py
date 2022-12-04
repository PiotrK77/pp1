file = open('07-FileHandling/numbers.txt', 'r')
copylines = open('07-FileHandling/copylines.txt', 'w')

for line in file:
    copylines.write(line)

file.close()
copylines.close()