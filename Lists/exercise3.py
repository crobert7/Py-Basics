import random
numbers = []

while len(numbers) <5:
    random_number = random.randint(1, 100)
    numbers.append(random_number)

for number in numbers: 
    print(number)
    if number > 90:
        print('Found at least one number greater than 90')
        break
else:
    print('No numbers greater than 90')

print('Complete')
