"""
Definition of Multiple Input O(n1 * n2) Time Complexity
An algorithm runs in O(n1 * n2) time if the number of operations it performs is 
directly proportional to more than 1 input which are independent of each other
n1 and n2 are the sizes of the two independent inputs.
"""


def pair_sum(array1, array2): # O(n1 * n2) Time Complexity
    sum = 0
    total_operations = 0

    for number1 in array1: # Outer loop runs n1 times
        for number2 in array2: # Inner loop runs n2 times
            sum += number1 * number2 # Constant time operation
            total_operations += 1
    return sum, total_operations

# This function creates a list [1, 2, ..., n]
def create_array(n):
    return list(range(1, n + 1))

# Test the functions for input arrays of increasing size from 1 to 10
for index1 in range(1, 6):
    numbers1 = create_array(index1)
    for index2 in range(1, 4):
        numbers2 = create_array(index2)
        _pair_sum, total_operations = pair_sum(numbers1, numbers2)  
        print(f"n1 = {index1}, n2 = {index2} Pair Operations = {total_operations}")

"""
Output:

n1 = 1, n2 = 1 Pair Operations = 1
n1 = 1, n2 = 2 Pair Operations = 2
n1 = 1, n2 = 3 Pair Operations = 3
n1 = 2, n2 = 1 Pair Operations = 2
n1 = 2, n2 = 2 Pair Operations = 4
n1 = 2, n2 = 3 Pair Operations = 6
n1 = 3, n2 = 1 Pair Operations = 3
n1 = 3, n2 = 2 Pair Operations = 6
n1 = 3, n2 = 3 Pair Operations = 9
n1 = 4, n2 = 1 Pair Operations = 4
n1 = 4, n2 = 2 Pair Operations = 8
n1 = 4, n2 = 3 Pair Operations = 12
n1 = 5, n2 = 1 Pair Operations = 5
n1 = 5, n2 = 2 Pair Operations = 10
n1 = 5, n2 = 3 Pair Operations = 15
"""
