# numbers = [1, 2, 4, 7]

# print(7 in numbers)
# print(6 in numbers)
# print(4 not in numbers)
# print(8 not in numbers)

# cities = ['LA', 'Berlin', 'Paris']

# for city in cities:
#     print(city)

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
    if number > 42:
        break
    print(number)