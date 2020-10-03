class Stack: 
    def __init__(self):
        # The double underscore made private the variable.
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val


object_stack = Stack()

object_stack.push(3)
object_stack.push(2)
object_stack.push(1)

print(object_stack.pop())

# This is a second stack.
stack_2 = Stack()
stack_2.push(1)
stack_2.push(2)
stack_2.push(3)

# SumStack inherits from Stack
class SumStack(Stack):
    def __init__(self):
        # Initialize the superclass
        Stack.__init__(self)
        self.__sum = 0
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

sum_stack = SumStack()

for i in range(5):
    sum_stack.push(i)
print(sum_stack.getSum())

for i in range(5):
    print(sum_stack.pop())

