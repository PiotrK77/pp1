number = int(input("Enter number: "))
product = None

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")