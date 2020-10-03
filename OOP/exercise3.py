# Class Variables 

class MyClass:
    __counter = 0

    def __init__(self, val = 1):
        self.__val = val
        MyClass.__counter += 1

object1 = MyClass()
object2 = MyClass(2)
object3 = MyClass(4)

print(object1.__dict__, object1._MyClass__counter) 
print(object2.__dict__, object2._MyClass__counter)
print(object3.__dict__, object3._MyClass__counter)