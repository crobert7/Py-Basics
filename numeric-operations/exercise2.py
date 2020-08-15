# first_value = int(input('First number: '))
# second_value = int(input('Second number: '))
# sum =first_value + second_value
# print('sum:' + str(sum))

# numeric_value = '7'
# print(numeric_value.isnumeric())

# string_value = 'Rob'
# print(string_value.isnumeric())

# Sum 
num1 = input('First number: ')
if num1.isnumeric() == False:
    print('Incorrect data type')
    exit()

num2 = input('Second number: ')
if num2.isnumeric() == False:
    print('Incorrect data type')
    exit()

num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print('Sum: ' + str(sum)) 

# Multiply 

x = input('First value: ')
y = input('Second value: ')

if x.isnumeric() == False or y.isnumeric() == False:
    print('Only numeric values')
    exit()

x = int(x)
y = int(y)

mult = x * y 
print(f'{x} times {y}: {mult}')