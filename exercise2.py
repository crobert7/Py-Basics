# print(type('Hello'))
# print(type(2))
# print(type(True))
# print(type('True'))
# print(type('False'))
# The bool() function converted the strings 'True' and 'False' to the Boolean values True and False. 
# When the function is supplied with an empty string, 
# it returns False, while any other non-empty string returns True.
# print(bool('True'))
# print(bool('False'))
# print(bool(''))
# print(bool(' '))
# print(bool('Hello'))

# The bool() function converts any non-zero value to True, but it converts the value 0 to False.

# print(bool(7))
# print(bool(1))
# print(bool(0))
# print(bool(-1))

# print(1 + 1 == 2)
# print(1 + 1 == 3)

# Comparison operators 

# print(3 == 4)
# print(3 != 4)
# print(3 > 4)
# print(3 < 4)
# print(3 >= 4)
# print(3 <= 4)

first_number = 5
second_number = 0
true_value = True
false_value = False 

if first_number > 1 and first_number < 10:
    print('The number is between 1 and 10')

if first_number > 1 or second_number < 1:
    print('At lest one value is geater than 1')

print(not true_value)
print(not false_value)

if first_number > 1 and second_number < 1:
    print('Both numbers pass the test')
else:
    print('Both values do not passs the test')