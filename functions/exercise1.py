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