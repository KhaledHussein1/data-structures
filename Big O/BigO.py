'''
Big O - Mathematical notion that describes the upper
bound (worst-case scenerio) of the time or space complexity 
of an algorithm in terms of the size of the input data.

O(1) > O(logn) > O(n) > O(n^2) > O(2^n)
'''
# O(1)
def constantTime(arr):
    print(arr[0]) #O(1)

# O(1 + 2n) --> O(n)
def linearTime(arr):
    print("Linear Time") #O(1)
    for i in range(len(arr)): #O(n)
        print(arr[i]) 
    for i in range(len(arr)): #O(n)
        print(arr[i]) 


# O(n^2)
def quadraticTime(arr):
    for i in range(len(arr)): # O(n)
        for i in arr: # O(n)
            print(i)

# O(logn)
def logarithmicTime(num, arr):
    # Binary Search Algorithm Implementation
    # Reduces work by half in every step
    high = len(arr)
    low = 0
    while low <= high:
        '''
        Shift (-), calculate middle, then shift back (+). Not
        necessary in python but good habit for other languages
        to prevent overflow with fixed-size integer types
        '''
        mid = low + (high-low)//2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            # New low is number to the right of mid
            low  = mid + 1
        else:
            # New high is number to the left of mid
            high = mid - 1
    return -1

# O(2^n)
def exponentialTime(n):
    # Recursive algorithm for computing the nth Fibonacci number
    if n <= 1:
        return n
    else:
        return exponentialTime(n-1) + exponentialTime(n-2)

# Test Functions:
# constantTime("text")
# linearTime([1,2,3])
# quadraticTime([1,2,3])
# print(logarithmicTime(6, [1,2,3,4,5,6]))
# print(exponentialTime(6))