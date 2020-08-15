import random

number = random.randint(1, 5)
tries = 0
user_input = 0

while number != user_input:
    tries = tries + 1
    user_input = input('Guessed a number between 1 and 5: ')
    if user_input.isnumeric() == False:
        continue
    
    user_input = int(user_input)

    if number == user_input:
        print(f'You win!')
        break
print(f'You guessed in {tries} tries')
        

        

