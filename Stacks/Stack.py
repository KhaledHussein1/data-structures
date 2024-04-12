'''Stack - Last In, First Out (LIFO)'''

class Stack():
    def __init__(self):
        self._stack = []

    @property
    def stack(self):
        # provide read-only access to the stack
        return self._stack.copy()
    
    @stack.setter 
    def stack(self, value):
        # prevent modifying stack directly to maintain integrity of its operations.
        raise ValueError("Cannot set stack directly")

    def is_empty(self): #O(1)
        return not self._stack

    def pop(self): #O(1)
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()

    def push(self, item): #O(1)
        self._stack.append(item)

    def peek(self): #O(1)
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._stack[-1]
    
    def __str__(self):
        return str(self._stack)


# Example usage:
my_stack = Stack()
try:
    print(my_stack.pop())
except IndexError as e:
    print(e)

my_stack.push(5) # bottom
my_stack.push(4)
my_stack.push(3)
my_stack.push(2) # top

print(my_stack)

my_stack.pop()

print(my_stack)

print(my_stack.pop())

print(my_stack.peek())

print(my_stack)

print(my_stack.is_empty())

my_stack.pop()
my_stack.pop()

print(my_stack.is_empty())

try:
    my_stack.stack = [1,2,3]
except ValueError as e:
    print(e)
