class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insertion
    def prepend(self, value): # O(n)
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1


    def append(self, value): # O(n)
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, value, index): # O(n/2) -> O(n)
        new_node = Node(value)

        if self.is_empty() or index > self.size - 1:
            raise IndexError("Index out of bound.")
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == (self.size-1):
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        elif index > (self.size // 2):
            current_node = self.tail
            for i in range((self.size - 1)- index):
                current_node = current_node.prev
            new_node.next = current_node
            new_node.prev = current_node.prev
            new_node.prev.next = new_node
            current_node.prev = new_node
        else:
            current_node = self.head
            while index != 0:
                index -= 1
                current_node = current_node.next
            new_node.next = current_node
            new_node.prev = current_node.prev
            new_node.prev.next = new_node
            current_node.prev = new_node
        self.size += 1
        return

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
        count = 0
        if self.is_empty():
            return 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

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

dll.append(13)
dll.append(14)
dll.append(15)

dll.insert(333, 7)
print(dll)






