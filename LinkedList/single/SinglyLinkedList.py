class Node:
    def __init__(self, data):
        self.data = data # the data the node is referencing
        self.next = None # initially not pointing to any other node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # Keep track of the head - empty on intialization
    
    '''
    Inserting Operations
    '''
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
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev_node = self.head
        current_index = 0

        while prev_node.next is not None and current_index < index - 1:
            prev_node = prev_node.next
            current_index += 1

        if prev_node is None or current_index != index - 1:
            raise IndexError("Index out of bounds")

        new_node.next = prev_node.next
        prev_node.next = new_node 
        
    
    '''
    Deleting Operations
    '''
    def remove_head(self): # O(1)
        current_node = self.head
        if current_node == None:
            raise IndexError("Can't remove from empty linked list!")
        self.head = current_node.next

    def remove_tail(self): # O(n)
        if self.is_empty():  
            raise IndexError("List is empty.")
    
        current_node = self.head
        if current_node.next is None: # If there's only one node, remove it
            self.head = None
            return
        
        # Traverse the list until the second to last node
        prev_node = None
        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
        
        # Remove the last node
        prev_node.next = None

    def remove(self, value): # O(n)
        if self.is_empty():
            raise IndexError("List is empty.")
        
        current_node = self.head
        prev_node = None
        
        while current_node is not None:
            if current_node.data == value:
                if prev_node is None:
                    self.head = current_node.next # Removing head node
                else:
                    prev_node.next = current_node.next # removing middle or tail
                return "Removed " + str(value)
            prev_node = current_node
            current_node = current_node.next

        return "value not found."
    
    '''
    Search Operation
    '''
    def search(self, value): # O(n)
        current_node = self.head
        index = 0

        if self.is_empty():
            raise IndexError("List is empty.")
        
        while current_node is not None:
            if current_node.data == value:
                return index
            index +=1
            current_node = current_node.next
        
        return -1 # If the value isn't found in any node
    
    '''
    Helper Operation
    '''
    def is_empty(self):
        current_node = self.head
        if current_node == None:
            return True
        return False
    
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    