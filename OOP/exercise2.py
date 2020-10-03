class ExampleClass:
    def __init__(self, val = 1):
        self.__primera = val
    
    def setSegunda(self, val):
        self.__segunda = val

object1 = ExampleClass()

object2 = ExampleClass(2)
object2.setSegunda(3)

object3 = ExampleClass(4)
object3.tercera = 5

print(object1.__dict__)
print(object2.__dict__)
print(object3.tercera)
