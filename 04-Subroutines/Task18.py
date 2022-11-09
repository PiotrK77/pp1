def countSumOfNumDig(number):
    length = len(str(number))
    sum = 0
    for i in range(0, length):
        sum += int(str(number)[i])
    return sum

print(countSumOfNumDig(7182))