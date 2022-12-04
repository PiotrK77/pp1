file = open('07-FileHandling/anyTextFile.txt', 'r')
fileContext = file.read()
print(fileContext)
file.close()