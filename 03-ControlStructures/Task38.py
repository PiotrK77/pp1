for i in range(1, 8):
    print(i, end = " ")
    
    for j in range(1, 7):
        if j < 6:
            print(i + j * 7, end = " ")
        else:
            print(i + j * 7)
