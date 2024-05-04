class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion 
    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node


    def append(self, value):
        pass

    def insert(self, value, index):
        pass

    # Deletion
    def remove_head(self):
        pass

    def remove_tail(self):
        pass

    def remove(self, index):
        pass

    # Traversal
    def search(self, value):
        pass

    # Helper Functions
    def length(self):
        pass

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    
dll = DoublyLinkedList()

dll.prepend(12)
dll.prepend(2)
dll.prepend(3)
dll.prepend(4)
dll.prepend(5)

print(dll)






