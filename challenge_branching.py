print('Would you like to continue?')
user_input = input()

if user_input == 'yes' or  user_input =='y':
    print('Continuing...')
    print('Complete!')
elif user_input == 'no' or  user_input == 'n':
    print('Exiting...')
else:
    print('Please try again and respond yes or no.')