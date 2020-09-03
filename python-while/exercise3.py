numeroSecreto = 777

print(
"""
+==================================+
| Welcome to my game, muggle!      |
| Enter an integer number          |
| and guess the number I choose    |
| For you.                         |
| by the way,                      |
| ¿Guess the number?               |
+==================================+
""")

num = int(input('Guess the number: '))

while numeroSecreto != num:
    print('Ja ja! You are in a infinity loop')
    num = int(input('Guess the number: '))
    
    if numeroSecreto == num:
        print('Good')

print(num)
