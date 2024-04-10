'''
An arry is stored as a contiguous sequence of bytes in memory.

Static Arrays are data structures with a fixed size determined at the 
time of creation, meaning their capacity cannot change during program 
execution. They provide fast access and modification of elements by 
index but require the size to be known upfront and do not allow resizing.

Dynamic Arrays are flexible data structures that can grow or shrink in size 
automatically as elements are added or removed. This adaptability comes with 
a slight performance overhead due to the need to occasionally reallocate and 
copy elements to new memory locations to accommodate size changes. In python
there are known as lists.
'''

# Python Collections (Arrays): List [], Tuple(), Set{}, Dictionary{key:value}

'''
Lists in Python are mutable, ordered collections of elements. Their dynamic 
size and ability to change contents make them highly flexible for storing and 
manipulating data. Lists support various operations, such as appending, removing, 
and sorting elements, facilitating dynamic data handling and manipulation 
in programming tasks.

list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[, start[, end]])
list.count(x)
list.sort(*, key=None, reverse=False)
list.reverse()
list.copy()

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
a = [1, 66.25, 333, 333, 1234.5]

del a[2:4]
a = [1, 66.25, 1234.5]

del a[:]
a = []

del a
Referencing the name a hereafter is an error 
(at least until another value is assigned to it).
'''
# Ordered, mutable, allows duplicates
# square brackets []
this_is_a_list = ["apple", "banna", "cherry", "cherry"] 
mixed_datatype_list = ["abc", 34, True, 40, "male"]

# From Python's perspective, lists are defined as objects with the data type 'list'
print(type(mixed_datatype_list))

# Using the list() constructor to make or convert to a List:
thislist = list(("apple", "banana", "cherry")) # tuple -> list


'''
Tuples are immutable, ordered collections of elements in Python. Their fixed 
size and inability to change after creation make them useful for storing data 
that should not be modified, allowing them to serve as keys in dictionaries and 
ensuring data integrity.


'''
# Ordered, immutable, allows duplicates
# round brackets ()
thistuple = ("apple", "banana", "cherry", "cherry")
tuple1 = ("abc", 34, True, 40, "male")

#To create a tuple with only one item, you have to add a comma 
# after the item, otherwise Python will not recognize it as a tuple.
is_a_tuple = ("apple",)
print(type(thistuple))
is_not_a_tuple = ("apple") # just a string
print(type(is_not_a_tuple)) 

#  tuple() method to make a or convert to a tuple
x = [1, 2, 3]
print(type(x))
x = tuple((x))
print(type(x))


'''
Sets are mutable, unordered collections of unique elements in Python. They 
are akin to mathematical sets, supporting operations like union, intersection, 
difference, and symmetric difference. Sets are optimal for membership testing,
removing duplicates from a sequence, and performing mathematical set operations. 
They do not record element position or allow duplicates, making them suitable 
for cases where the existence of an item in a collection is more significant than 
the order or frequency of items Set items can appear in a different order every 
time you use them, and cannot be referred to by index or key.
'''
# Unordered, immutable*, no duplicates
# *Set items are immutable, but you can remove and/or add items
# Curly braces {}
thisset = {"apple", "banana", "cherry"}
set1 = {"abc", 34, True, 40, "male"}

# Note: the values True and 1 are considered the same value in sets, and are treated as 
# duplicates. Same thing for False and 0:
thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(thisset)

# Using the set() constructor to make a set (typle -> set):
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

'''
Dictionaries are mutable, unordered collections of key-value pairs in Python. 
Each key-value pair maps the key to its associated value, making dictionaries ideal 
for storing data that can be retrieved without knowing its index position. Keys in 
a dictionary must be unique and immutable types, allowing them to serve as efficient 
lookup references. Dictionaries are highly flexible, supporting the modification of data, 
and are used extensively for representing real-world data structures in programming, 
such as records, nodes in graphs, or attributes and their values.
'''
# Ordered, mutable, no duplicates (same key not allowed)
# Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Written with curly brackets, and have keys and values: { key : value }
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Can be referred to by using the key name:
print(thisdict["brand"])

# Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
