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
    def prepend(self, value): # O(1)
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


    def append(self, value): # O(1)
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
        if self.is_empty() or index > self.size - 1:
            raise IndexError("Index out of bound.")
        elif index == 0:
            self.prepend(value)
        elif index == (self.size-1):
            self.append(value)
        else:
            new_node = Node(value)
            if index > (self.size // 2):
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
    def remove_head(self): # O(1)
        if self.is_empty():
            raise IndexError("Can't remove from empty linked list!")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove_tail(self): # O(1)
        if self.is_empty():
            raise IndexError("Can't remove from empty linked list!")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def remove(self, index): # O(n/2) -> O(n)
        if self.is_empty() or index > self.size - 1:
            raise IndexError("Index out of bound.")
        elif index == 0:
            self.remove_head()
        elif index == (self.size-1):
            self.remove_tail()
        elif index > (self.size // 2):
            current_node = self.tail
            for i in range((self.size - 1)- index):
                current_node = current_node.prev
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        else:
            current_node = self.head
            while index != 0:
                index -= 1
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        self.size -= 1
        return

    # Traversal
    def search(self, value):
        if self.is_empty():
            return False
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == value:
                    return True
                current_node = current_node.next
        return False

    # Helper Function
    def is_empty(self): # O(1)
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
    

if __name__ == "__main__":
    dll = DoublyLinkedList()


    dll.prepend(12)

    dll.append(1)
    dll.append(3)
    dll.append(2)
    dll.append(6)
    dll.append(7)
    dll.append(9)
    dll.append(199)
    dll.remove(4)
    print(dll)
    






