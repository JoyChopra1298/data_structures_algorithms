"""
Definition of Constant O(1) Time Complexity
An algorithm runs in O(1) time if the number of operations it performs is 
independent of the size of the input n
"""

def head(array):
    total_operations = 0

    # The operation to access the first element of the array is constant time
    head_element = array[0] # Constant time operation
    total_operations += 1

    return head_element, total_operations

# This function creates a list [1, 2, ..., n]
def create_array(n):
    return list(range(1, n + 1))

# Test the head function for arrays of increasing size from 1 to 10
for index in range(1, 11):
    numbers = create_array(index)
    sum, total_operations = head(numbers)
    print(f"n = {index}, Operations = {total_operations}")

"""
Output:

n = 1, Operations = 1
n = 2, Operations = 1
n = 3, Operations = 1
n = 4, Operations = 1
n = 5, Operations = 1
n = 6, Operations = 1
n = 7, Operations = 1
n = 8, Operations = 1
n = 9, Operations = 1
n = 10, Operations = 1
"""