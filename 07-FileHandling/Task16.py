file = open('07-FileHandling/numbers.txt', 'r')
copy = open('07-FileHandling/copy.txt', 'w')


copy.write(file)

file.close()
copy.close()
