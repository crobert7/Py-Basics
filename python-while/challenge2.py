import random
number = random.randint(1, 10)
user_input = 0
tries = 0
print('Guess the number between 1 and 10')

while number != user_input:
    tries += 1
    user_input = input(f'Enter guess #{tries}: ')

    if user_input.isnumeric() == False:
        print('Only numeric values.')
        continue
    
    user_input = int(user_input)

    if user_input < number:
        print('Your guess is too low, try again.')
        continue
    elif user_input > number: 
        print('Your guess is to high, try again.')
        continue
else:
    print(f'You guessed it in {tries} tries.')

