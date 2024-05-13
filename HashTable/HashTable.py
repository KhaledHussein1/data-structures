class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacitiy = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, value):
        pass

    def search(self, value):
        pass

    def remove(self, value):
        pass

    def __str__(self):
        pass

