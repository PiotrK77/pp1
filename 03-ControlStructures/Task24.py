amount = int(input("Enter the amount in PLN: "))
PLN = amount
coin5 = None
coin2 = None
coin1 = None
rest = None

coin5 = amount // 5
amount %= 5

coin2 = amount // 2
amount %= 2

coin1 = amount

print(f"The amount of PLN {PLN} in coins:\n5 zł - {coin5}\n2 zł - {coin2}\n1zł - {coin1}")
