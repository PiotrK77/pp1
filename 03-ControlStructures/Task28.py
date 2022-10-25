for i in range(1, 31):
    if i % 3 == 0:
        print("THREE", end = " ")
    if i % 5 == 0:
        print("FIVE", end = " ")
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO", end = " ")
    else:
        print(i, end = " ")