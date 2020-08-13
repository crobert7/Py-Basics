first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
aux1 = f'{first_value.title():>31}'
# print(aux1)
# Another way to solve the first challenge
first_value = first_value.strip()
first_value = first_value.lower()
first_value = first_value.title()
first_value = f'{first_value:^30}' # ^ forces the field to be centered within the available space
print(first_value)

# Second Challenge 
aux2 = f'{second_value.replace(" ", "", 2).strip("-").capitalize():<20}'
# print(aux2)
# Another way to solve the second challenge
second_value = second_value.replace('-', '')
second_value = second_value.strip()
second_value = second_value.capitalize()
print(second_value)

# Third challenge
aux3 = f'{third_value.replace(" ", "").replace("-", " ").capitalize():>30}'
# print(aux3)
# Another way to solve the third chellenge
third_value = third_value.replace(' ', '')
third_value = third_value.replace('-', ' ')
third_value = third_value.swapcase()
third_value = f'{third_value:>30}'
print(third_value)

# Fourth challenge
# print(fourth_value+'#'+fifth_value+'#'+sixth_value+'!')
# Another way to solve the fourth challenge
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth Challenge
print(f'\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
