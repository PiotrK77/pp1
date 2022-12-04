array = [5,4,3,2,6,5]

def arrToStr(array):
    string = ""
    for i in array:
        string += str(i)
        string += ", "
    string = string[0: len(string) - 2]
    return string

print(arrToStr(array))