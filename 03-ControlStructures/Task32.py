code = "0805"
for i in range(1, 4):
    inputPIN = input("Enter the PIN code: ")
    if inputPIN == code:
        print("Correct")
        break
    else:
        print("Incorrect")

