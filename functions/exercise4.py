# function scope
# variables defined outside a function don't affect variables defined inside a function 
# unless your code returns the inside value and then uses it. 
# The scope of a function's variables is sealed off 
# and hidden from code outside the function and the other way around.

value = 1

def some_function():
    value = 10
    return value

print(value)
some_function
print(value)

def f(par2, par1):
    return par2 + par1

# print(f(par2 = 1, 5))