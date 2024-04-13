class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            # Set the new node's next to the current head
            new_node.next = self.head
            # Update the head to be the new node
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        current_node = self.head

        if self.head == None:
            self.head = new_node
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
    
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    
# example usage
ll = SinglyLinkedList()
ll.append(2)
ll.append(8)
ll.append(99)

ll.prepend(99)

print(ll)