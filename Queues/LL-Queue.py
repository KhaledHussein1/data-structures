import sys
sys.path.append('C:/Users/Masch/Desktop/Data Structures')  
from LinkedList.double.DoublyLinkedList import DoublyLinkedList as DLL

class Queue:
    def __init__(self):
        self.dll = DLL()

    def enqueue(self): # O(1)
        self.dll.remove_head()

    def dequeue(self, value): # O(1)
        self.dll.append(value)

    def is_empty(self): # O(1)
        return self.dll.is_empty()
    
    def __str__(self):
        nodes = []
        current = self.dll.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " <-- ".join(nodes)
    
q = Queue()
