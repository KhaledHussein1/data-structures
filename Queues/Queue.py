# Queue - First In, First Out (FIFO)

class Queue():
    def __init__(self):
        self._queue = []

    @property
    def queue(self):
        return self._queue.copy()
    
    @queue.setter 
    def queue(self, value):
        # prevent modifying queue directly to maintain integrity of its operations.
        raise ValueError("Cannot set queue directly")

    def enqueue(self, x): #O(1)
        self._queue.append(x)

    def dequeue(self): #O(n) due to shifting!!!
        if not self._queue:
            raise IndexError("cannot dequeue empty queue.")
        return self._queue.pop(0)
    
    def __str__(self):
        return str(self._queue)

my_queue = Queue()

my_queue.enqueue(1) # head
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6) # tail

print(my_queue)

my_queue.dequeue()

print(my_queue)

try: 
    my_queue.queue = [3,2,1]
except ValueError as e:
    print(e)

print(my_queue.queue)