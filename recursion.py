def summation(n):
    # base case
    if n <= 0:
        return 0
    # recursive case
    else:
        return n + summation(n - 1)

summ = summation(3)
print(summ)

def factorial(n):
    # base case
    if n <= 1:
        return 1
    # recursive case 
    else:
        return n * factorial(n -1)

fact = factorial(3)
print(fact)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibo = fibonacci(3)
print(fibo)

def exponentiation(n, exp):
    if exp <= 0:
        return 1
    else:
        return n * exponentiation(n, exp - 1) 

exp = exponentiation(5,4)
print(exp)
