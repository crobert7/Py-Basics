num = 5
num2 = 4

sum = num + num2
diff = num - num2
product = num * num2
quotient = num / num2
modulus = num % num2
exponent = num ** num2
print('Sum: ' + str(sum))
print('Difference: ' + str(diff))  
print('Product: ' + str(product)) 
print('Quotient: ' + str(quotient)) 
print('Modulus: ' + str(modulus)) 
print('Exponent: ' + str(exponent)) 

# Python follow PEMDAS acronym, which indicates the order in which the operations hould be perfomed
# P arenthesis: Resolve operations between parenthesis first
# E xponent: Resolve exponents
# M ultiplication: Perform multiplications from left ot fight
# D ivision: Perform division from left to right
# A ddition: Perform addition from left to right 
# S ubtraction: Perform subtraction from left to right

print(3 + 4 * 5)
print((3 + 4) * 5)

pi = 3.14 
print(type(pi))
print(int(pi))
print(round(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
print(round(uptime))

a = round(7.654321, 2)
print(a)

b = round(9.87654, 3)
print(b)