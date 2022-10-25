numberOfNumbers = 0
sum = 0
quantity = 0
mean = 0

while True:
    number = int(input("Enter number: "))
    if number == 0:
        mean = sum / quantity
        break
    else:
        quantity += 1
        sum += number

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")
