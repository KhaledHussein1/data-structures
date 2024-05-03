class Node:
    def __init__(self, data):
        self.data = data # the data the node is referencing
        self.next = None # initially not pointing to any other node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # Keep track of the head - empty on intialization

    def is_empty(self):
        current_node = self.head
        if current_node == None:
            return True
        return False
        
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
    
    # Add at a specific index - O(n)
    def insert(self, value, index):
        new_node = Node(value)
        i = 0

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        while current_node != None:
            prev_node = current_node
            current_node = current_node.next
            if i == index:
                prev_node.next = new_node
                new_node.next = current_node.next
                return
            elif i <= index:
                i+=1
        return
    
    def remove_head(self): # O(1)
        current_node = self.head
        if current_node == None:
            raise IndexError("Can't remove from empty linked list!")
        self.head = current_node.next

    def remove_tail(self): # O(n)
        current_node = self.head
        prev_node = None
        if self.is_empty():
            raise IndexError("List is empty.")
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None

    def remove(self, value):
        index = 0
        current_node = self.head

        # When the ll is empty or the value is the head
        if self.is_empty():
            raise IndexError("List is empty.")
        elif current_node.data == value:
            self.head = current_node.next
            return "removed " + str(value) + " at index " + str(index)
        
        # When the value is between the head and tail
        while current_node.next != None:
            if current_node.data == value:
                prev_node.next = current_node.next
                return "removed " + str(value) + " at index " + str(index)
            index+=1
            prev_node = current_node
            current_node = current_node.next

        # When the value is the tail
        if current_node.data == value:
            prev_node.next = None
            return "removed " + str(value) + " at index " + str(index)
        
        # When the value doesn't exist
        return "value not found."
    
    def search(self, value): # O(n)
        current_node = self.head
        index = 0

        if self.is_empty():
            raise IndexError("List is empty.")
        
        while current_node.next != None:
            if current_node.data == value:
                return index
            index +=1
            current_node = current_node.next
        
        # When the value is the tail
        if current_node.data == value:
            return index
        return -1
     
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
ll.append(728)

print(ll)

try:
    ll.insert(6696,1)
except IndexError as e:
    print(e)

print(ll)
