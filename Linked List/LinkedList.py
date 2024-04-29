class Node:
    def __init__(self, data):
        self.data = data # the data the node is referencing
        self.next = None # initially not pointing to any other node

'''
append(value)
prepend(value)
insert(value, index)
'''
class SinglyLinkedList:
    def __init__(self):
        self.head = None # Keep track of the head - empty on intialization

    # Add at the beginning of linked list - O(1)
    def prepend(self, value): 
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            # Set the new node's next to the current head - (new_node -> (head -> current_head_node))
            new_node.next = self.head
            # Update the head to be the new node - (head -> new_node -> current_head_node)
            self.head = new_node

    # Add at the end of linked list - O(n) - can be O(1) if we have a tail pointer
    def append(self, value): 
        new_node = Node(value)
        current_node = self.head

        if self.head == None:
            self.head = new_node
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
    
    # Add after a specific index - O(n)
    def insert(self, value, index):
        new_node = Node(value)
        current_node = self.head
        i = 0

        while current_node is not None:
            if i == index:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            elif i <= index:
                i+=1
                current_node = current_node.next
        raise IndexError("Index out of bound!")
    
    def remove_head(self): # O(1)
        current_node = self.head
        if current_node == None:
            raise IndexError("Can't remove from empty linked list!")
        self.head = current_node.next

    def remove_tail(self): # O(n)
        current_node = self.head
        prev_node = None
        if current_node == None:
            raise IndexError("Can't remove from empty linked list!")
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
     
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    
# example usage
ll = SinglyLinkedList()

try:
    ll.remove_head()
except IndexError as e:
    print(e)

ll.append(2)
ll.append(8)
ll.append(99)

ll.prepend(99)

print(ll)

try:
    ll.insert(666,2)
except IndexError as e:
    print(e)

ll.remove_tail()
print(ll)

