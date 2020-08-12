from datetime import date

print("Today's date?")
date = date.today()
print(date)

print('Breakfast Calories?')
breakfast_calories = int(input())

print('Dinner Calories?')
dinner_calories = int(input())

print('Snack Calories?')
snack_calories = int(input())

calories_sum = breakfast_calories + dinner_calories + snack_calories

print('Calorie content for ' + str(date) + ': ' + str(calories_sum))

