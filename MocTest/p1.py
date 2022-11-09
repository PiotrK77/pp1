def card_number(card):
    card = card[0:2] + "**********" + card[12:16]
    print(card)

card_number("5290312400019022")

