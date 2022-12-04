array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def evenodd(array):
    even = []
    odd = []
    evenoddArr = []
    for i in array:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)
    for i in even:
        evenoddArr.append(i)
    for i in odd:
        evenoddArr.append(i)

    print(evenoddArr)

evenodd(array)