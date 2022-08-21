lst = [1,2,3]

def add_to_list(input_lst, items):
    input_lst = lst
    input_lst.append(items)
    return input_lst

fn = add_to_list(lst, 4)

print(lst)
print(fn)

# Reverse a function with slice function

# slice str[start:stop:step]
trial = 'reversal'

# to let know python use the entire string we use ::
new_trial = trial[::-1]
print(new_trial)

# Reverse function with recursion

def str_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str_reverse(str[1:]) + str[0]

rev = str_reverse('reverse')

print(rev)

# map and filter 

coffee_menu = ['espresso', 'lette', 'capuccino', 'mocha', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# the first argument of the map function is the function itself and the second paramater the iterable object
# we are passign the function as an argument not calling the function 
map_coffee = map(find_coffee, coffee_menu)

print(map_coffee)
# Loop through the object

for i in map_coffee:
    print(i)

filter_coffee = filter(find_coffee, coffee_menu)
print(filter_coffee)

for i in filter_coffee:
    print(i)

# Comprehensions 
# A way to create new sequences from an already existing sequence

# There are four main types of comprehensions in Python: 

# List comprehension 
# Dictionary comprehension 
# Set comprehension 
# Generator comprehension

# List comprehension
# Syntax: [<expression> for x in <sequence> if <condition>] 

data = [2,3,5,7,11,13,17,19,23,29,31]

# Updating the list 
data = [i+3 for i in data]

print(data)

# Creating new list 
new_data  = [x * 3 for x in data]
print(new_data)

# With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0]
print("Divisible by four", fourx)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

# Dictionary comprehension
# Syntax: dict = { key:value for key, value in <sequence> if <condition> } 

# Using range() function and no input list
using_range = {x:x*2 for x in range(10)}
print(using_range)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

months_dict = { key:value for (key,value) in zip(number,months) }
print("Using two lists: ", months_dict)

# Set comprehension
# Syntax { <expression> for x in <sequence> if <condition> }

set_a = { x for x in range(10, 20) if x not in [12, 14, 16] }
print('Using set', set_a)


# Generator comprehension
# Syntax: ( <expression> for <expression> in <sequence> )

gen = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in gen)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")