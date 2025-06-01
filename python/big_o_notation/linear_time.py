"""
Definition of Linear O(n) Time Complexity
An algorithm runs in O(n) time if the number of operations it performs is 
directly proportional to the size of the input n
"""

def linear_sum(array):
    sum = 0
    total_operations = 0

    # Let n be the size of the input array
    # The sum operation inside the loop takes constant time,
    # and the loop runs 'n' times.
    # Hence the total time is proportional to n
    for number in array:
        sum += number   # Constant time operation
        total_operations += 1
    return sum, total_operations

# This function creates a list [1, 2, ..., n]
def create_array(n):
    return list(range(1, n + 1))

# Test the linear_sum function for arrays of increasing size from 1 to 10
for index in range(1, 11):
    numbers = create_array(index)
    sum, total_operations = linear_sum(numbers)
    print(f"n = {index}, Operations = {total_operations}")

"""
Output:

n = 1, Operations = 1
n = 2, Operations = 2
n = 3, Operations = 3
n = 4, Operations = 4
n = 5, Operations = 5
n = 6, Operations = 6
n = 7, Operations = 7
n = 8, Operations = 8
n = 9, Operations = 9
n = 10, Operations = 10
"""