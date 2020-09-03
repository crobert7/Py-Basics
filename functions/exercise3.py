# functions returns a single value

def create_deck():
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    return deck

my_deck = create_deck()
print(len(my_deck))