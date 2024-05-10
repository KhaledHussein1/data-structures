import sys
#sys.path.append('')  
from LinkedList.double.DoublyLinkedList import DoublyLinkedList as DLL

class Queue:
    def __init__(self):
        self.dll = DLL()

    def pop(self):
        self.dll.remove_head()

    def push(self, value):
        self.dll.prepend(value)

    def is_empty(self):
        return self.dll.is_empty()
    
q = Queue()

print(q.is_empty())