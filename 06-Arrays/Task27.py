array = [5,1,9,6,1]
largest = None
smallest = None

for i in array:
    if largest == None:
        largest = i
    if smallest == None:
        smallest = i
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(largest - smallest)