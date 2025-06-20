"""
Definition of Logarithmic O(logn) Time Complexity
An algorithm runs in O(logn) time if the number of operations it performs is 
directly proportional to the logarithm of n, where n is the size of the input
"""

import random

def binary_search(array, target):  # O(logn) Time Complexity
    low = 0
    high = len(array) - 1
    total_operations = 0

    while low <= high:
        mid = (low + high) // 2
        total_operations += 1
        
        if array[mid] == target:
            return mid, total_operations
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, total_operations


# This function creates a list [1, 2, ..., n]
def create_array(n):
    return list(range(1, n + 1))

# Test the head function for arrays of increasing size from 1 to 10
for index in range(1, 33, 2):
    numbers = create_array(index)
    target = random.randint(0, index-1)
    sum, total_operations = binary_search(numbers, target=index)  # Assuming we are searching for the index itself
    print(f"n = {index}, Operations = {total_operations}")

"""
Output:

n = 1, Operations = 1
n = 3, Operations = 2
n = 5, Operations = 3
n = 7, Operations = 3
n = 9, Operations = 4
n = 11, Operations = 4
n = 13, Operations = 4
n = 15, Operations = 4
n = 17, Operations = 5
n = 19, Operations = 5
n = 21, Operations = 5
n = 23, Operations = 5
n = 25, Operations = 5
n = 27, Operations = 5
n = 29, Operations = 5
n = 31, Operations = 5
"""
