def say_hello():
    print('Hello world!')

say_hello()

# function with input parameter
def hello_name(name):
    print(f'hello {name}!')

hello_name('Rob')

# function with optional parameter
def hello(name='country'):
    print(f'hello {name}')

hello()

# function with a second optional parameter
def sayHello(name = 'World', greeting = None):
    if greeting == None:
        print(f'Hello, {name}')
    else:
        print(f'{greeting} {name}')

sayHello()
sayHello('Rob')
sayHello(greeting = 'Good day')
sayHello('Robert', 'Nites!')

print(type(None))


# function that return a single value 
def add_two_numbers(x, y):
    return x + y 

add_two_numbers(4,6)
result = add_two_numbers(5, 7)
print(result)