print('Simple Calculator!')

x = input('First number?')
if x.isnumeric() == False:
    print('Please input a numer,')
    exit()

operator = input('Operation?')

y = input('Second number?')
if y.isnumeric() == False:
    print('Please input a number.')
    exit()

x = int(x)
y = int(y)

if operator == '+':
    sum = x + y
    print(f'Sum of {x} + {y} equals: {sum}')

elif operator == '-':
    sustraction = x - y
    print(f'Sustraction of {x} - {y} equals: {sustraction}')

elif operator == '*':
    product = x * y
    print(f'Product of {x} * {y} equals: {product}')

elif operator == '/':
    quotient = x / y
    print(f'Quotient of {x} / {y} equals: {quotient}')

elif operator == '%':
    modulus = x % y
    print(f'Modulus of {x} % {y} equals: {modulus}')

elif operator == '**':
    exp = x ** y
    print(f'Exponent of {x} ** {y} equals: {exp}')

else: 
    print('Operation not recognized')
    exit()