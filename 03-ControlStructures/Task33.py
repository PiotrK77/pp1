for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()

i = 6
j = 1

while i > -3:
    while j < 4:
        print(f" {i+j}", end = "")
        j += 1
    i -= 3
    j = 1
    print()
