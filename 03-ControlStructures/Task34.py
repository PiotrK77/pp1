a = 0
b = 1
c = None


for i in range(1, 50):
    if i == 1:
        print(a, b, end = " ")
    else:
        c = a + b
        print(c, end = " ")
        a = b
        b = c

