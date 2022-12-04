meatAndFish = open("07-FileHandling/MeatAndFish.txt", "r")
GrainsAndBread = open("07-FileHandling/GrainsAndBread.txt", "r")
shoppinglist = open("07-FileHandling/shoppinglist.txt", "w")

for lines in meatAndFish:
    shoppinglist.write(lines)
shoppinglist.write("\n")
for lines in GrainsAndBread:
    shoppinglist.write(lines)
meatAndFish.close()
GrainsAndBread.close()
shoppinglist.close()