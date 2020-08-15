# celsius = (fahrenheit - 32) * 5/9

fahrenheit = input('What\'s the temperature in Fahrenheit: ')
if fahrenheit.isnumeric() == False:
    print('Input is not a number.')
    exit()

fahrenheit = int(fahrenheit)
celsius = (fahrenheit - 32) * 5/9
celsius = int(celsius)
print(f'The temperature in celsius is: {celsius}')

# fahrenheit = (celsisus * 9/5) + 32

# celsius = input('What\'s the temperature in Celsius: ')
# if celsius.isnumeric() == False:
#     print('Input is not a number')
#     exit()

# celsius = int(celsius)
# fahrenheit = (celsius * 9/5) + 32
# fahrenheit = int(fahrenheit)
# print(f'The temperature in Celsius is: {fahrenheit}')