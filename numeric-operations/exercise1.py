# print(type('7'))
# print(type(7))
# print(type(7.1))

# The isinstance function, allows you to assert that you expect a value to be a certain data type.
# The isinstance function return True or False 
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))
print(isinstance('7', int))
print(isinstance(7.1, int))

# Another technique to evaluate the current data type
print(type('7') == str)
print(type(7) == float)

# It is important to understand that te data type is part of the value, but the data type is not part of the variable.
# A variable can point to any value, regardless of the vaule's the data type

x = 'a string'
print(type(x)) 
x = 7
print(type(x))
x = True 
print(type(x))