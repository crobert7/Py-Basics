# msg = str.capitalize('first message')
# print(msg)
# msg = 'second message'.capitalize()
# print(msg)
# msg = 'third message'
# print(msg.capitalize())

# msg = 'hello world'
# print(msg.upper())
# print(msg.lower())
# msg = msg.title()
# print(msg)
# print(msg.swapcase())

# location = 'Mississippi'
# print(location.count('s'))

# print(len('How many letters in this string?'))

# msg = 'racecar'
# print(msg.startswith('r'))
# print(msg.endswith('a'))

# message = 'The quick brown fox jumps over the lazy dog'
# print(message.find('q'))

# print(message.find('t'))
# print(message.find('T'))

# message = '    middle     '
# print('.' + message.lstrip() + '.') # remove left side empty space characters
# print('.' + message.rstrip() + '.') # remoce rigth side empty space characters
# print('.' + message.strip() + '.') # remove both sides empty space characters

# replace() swaps every instance of a string with a different string.
# message = 'brevity is the essence of wit'
# message = message.replace('essence', 'soul')
# print(message)


# The rjust() and ljust() methods add empty space characters to a string to provide justification to the right or left, 
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))


