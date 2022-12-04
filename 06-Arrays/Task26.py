array = [5, 1, 9, 6, 1]
secondHighest = None
highest = None

for i in array:
    if highest == None:
        highest = i
    elif secondHighest == None and i < highest:
        secondHighest = i
    elif i > highest:
        highest = i
    elif i > secondHighest:
        secondHighest = i

print(secondHighest)