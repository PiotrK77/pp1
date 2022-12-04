fileName = input("Enter file name: ")

file = open(f"07-FileHandling/{fileName}",  "r")
lines = 0
for line in file:
    lines += 1
file.close()
print(f"File name: {fileName}\nNumber of lines: {lines}")