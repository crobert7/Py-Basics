# Nested for loop

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']

for suit in suits:
    for rank in ranks:
        print(f'{rank} of {suit}')
