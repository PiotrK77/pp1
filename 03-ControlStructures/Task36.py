number = int(input("Enter amount of numbers: "))

print("Prime numbers: ", end = "")

for i in range(1, number + 1):
    if i > 1:
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            print(i, end = " ")
