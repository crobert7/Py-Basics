# You define a list by using a set of square brackets []. Inside the brackets, you add values. SEparate the values with commas.
colors = ['blue', 'yellow', 'green', 'orange', 'purple', 'pink']
print(colors)
print(type(colors))

print(f'0-based indexing into the list... second item: {colors[1]}')
print(f'Last item of the list {colors[-1]}')
print(f'Next to the last item in the list {colors[-2]}')

# Calling these functions permanently changes the order in which the elements of the list are stored in memory.
colors.reverse()
print(colors)
colors.sort()
print(colors)
color = colors.pop(0)
print('Popped first item', color)
color = colors.pop(-1)
print('Popped last item', color)
colors.append('magenta')
colors.append('cyan')
colors.remove('pink')
print(colors)

sundry = ['Rob', 7, 9.90, False]
print(sundry)
print(type(sundry))

# Empty list
my_list= []
print(my_list)

# Create a slice
food = ['pizza', 'burger', 'tacos', 'pasta', 'bread', 'hot-dog', 'jelly']
print('\nPrint a SLICE, starting at index 2 and excluding index5')
print(food[2:5])
print(type(food[2:5]))

print('\nPrint a SLICE, starting at index 0 to index 3')
print(food[:3])

print('\nPrint a SLICE, starting at index 4 to the end of the list')
print(food[4:])

print('\nPrint a slice, from the 4th from the end up until the last item:')
print(food[-4:-1])

# Combining new list with an existing list
coolors = ['cyan', 'gray', 'magenta', 'blue', 'green', 'orange', 'purple']
new_coolors = ['lime', 'carmine']
coolors.extend(new_coolors)
print(coolors)
# Clearing the list
coolors.clear()
print(coolors)
