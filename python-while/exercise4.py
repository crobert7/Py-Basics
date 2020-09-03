word = input('Type a word: ')

while word != 'chupacabra':
    word = input('Type a word: ')
    if word == 'chupacabra':
        print('You are out of the loop')
        break