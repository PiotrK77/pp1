

def binary_number(number):
    length = len(number)
    isBinary = None
    for i in range(0, length):
        if number[i] == "1" or number[i] == "0":
            pass
        else:
            isBinary = False
            print(isBinary)
            return False
    isBinary = True
    print(isBinary)

binary_number("101fdfdf01")
    

