import sys
sys.path.append('C:/Users/Masch/Desktop/Data Structures')  
from LinkedList.double.DoublyLinkedList import DoublyLinkedList as DLL

class Queue:
    def __init__(self):
        self.dll = DLL()

    def pop(self):
        self.dll.remove_head()

    def push(self, value):
        self.dll.append(value)

    def is_empty(self):
        return self.dll.is_empty()
    
    def __str__(self):
        nodes = []
        current = self.dll.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " <-- ".join(nodes)
    
q = Queue()

print(q.is_empty())
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)

print(q)
q.pop()

print(q)