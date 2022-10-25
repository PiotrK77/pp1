a = 4
b = 15


for i in range(1, b + 1):
    if i == b:
        print("*")
    else:
        print("*", end = "")


for a in range(1, a + 1):
    for i in range(1, b):
        if i == 1:
            print("*", end = "")
        if i == b - 1:
            print("*")
        else:
            print(" ", end = "")

for i in range(1, b + 1):
    if i == b:
        print("*")
    else:
        print("*", end = "")