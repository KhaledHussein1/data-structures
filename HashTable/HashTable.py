class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
# Important to choose good hash function to avoid O(n)
class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key): # O(1)
        return hash(key) % self.capacity

    def insert(self, key, value): # O(n) but O(1) w/ evenly distributed keys
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key): # O(n) but O(1) w/ evenly distributed keys
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key): # O(n) but O(1) w/ evenly distributed keys
        index = self._hash(key)

        previous = None 
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            chain = []
            while current:
                chain.append(f"({current.key}: {current.value})")
                current = current.next
            if chain:
                elements.append(f"Index {i}: " + " -> ".join(chain))
        return "\n".join(elements)

h = HashTable(11)
for i in range(50):
    h.insert(i+1,i)

print(h)