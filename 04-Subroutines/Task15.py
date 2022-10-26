import mymath

print("Guess number fro 1 to 9, to exit type 0")

while True:

    x = mymath.generateNumber()
    y = mymath.readNumber()

    if y == 0:
        print("Bye")
        break
    if x == y:
        print("You won!")
    if x != y:
        print("Try again")
