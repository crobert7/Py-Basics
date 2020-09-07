import math

# static method
root = math.sqrt(4)
print(root)

class mathops:
    @staticmethod
    def square(val):
        return val * val

square = mathops.square(6)
print(square)

