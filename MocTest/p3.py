def amount_to_pay(amount):


    remaining = amount % 5
    coin5 = (amount - remaining) / 5
    amount = remaining
    remaining = amount % 2
    coin2 = (amount - remaining) / 2
    coin1 = remaining

    print(int(coin5 + coin2 + coin1))



amount_to_pay(28)
