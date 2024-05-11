import sys
sys.path.append('C:/Users/Masch/Desktop/Data Structures')  
from LinkedList.double.DoublyLinkedList import DoublyLinkedList as DLL

class Stack:
    def __init__(self):
        self.dll = DLL()
    
    def pop(self): # O(1)
        self.dll.remove_tail()

    def push(self, value): # O(1)
        self.dll.append(value)
    
    def is_empty(self): # O(1)
        return self.dll.is_empty()
    
    def peek(self): # O(1)
        if self.dll.is_empty():
            raise IndexError("Empty Stack!")
        return self.dll.tail.data

    def __str__(self):
        return str(self.dll)
    
s = Stack()

for i in range(5):
    s.push(i)

print(s)

s.pop()

print(s)

print(s.is_empty())

print(s.peek())

print(s)