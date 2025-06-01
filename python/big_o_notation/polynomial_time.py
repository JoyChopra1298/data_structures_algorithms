"""
Definition of Polynomial O(n^k) Time Complexity
An algorithm runs in O(n^k) time if the number of operations it performs is 
directly proportional to a polynomial F(n) in n with degree k,
where n is the size of the input and k is a constant greater than 1.
"""


def pair_sum(array): # O(n^2) Time Complexity
    sum = 0
    total_operations = 0

    for number1 in array: # Outer loop runs n times
        for number2 in array: # Inner loop also runs n times
            sum += number1 * number2 # Constant time operation
            total_operations += 1
    return sum, total_operations

def triplet_sum(array): # O(n^3) Time Complexity
    sum = 0
    total_operations = 0

    for number1 in array: # Outer loop runs n times
        for number2 in array: # Middle loop runs n times
            for number3 in array: # Inner loop also runs n times
                sum += number1 * number2 * number3 # Constant time operation
                total_operations += 1
    return sum, total_operations

# This function creates a list [1, 2, ..., n]
def create_array(n):
    return list(range(1, n + 1))

# Test the functions for input arrays of increasing size from 1 to 10
for index in range(1, 11):
    numbers = create_array(index)
    _pair_sum, quadratic_total_operations = pair_sum(numbers)
    _triplet_sum, cubic_total_operations = triplet_sum(numbers)
    print(f"n = {index}, Pair Operations = {quadratic_total_operations}"
          f" Triplet Operations = {cubic_total_operations}")

"""
Output:

n = 1, Pair Operations = 1 Triplet Operations = 1
n = 2, Pair Operations = 4 Triplet Operations = 8
n = 3, Pair Operations = 9 Triplet Operations = 27
n = 4, Pair Operations = 16 Triplet Operations = 64
n = 5, Pair Operations = 25 Triplet Operations = 125
n = 6, Pair Operations = 36 Triplet Operations = 216
n = 7, Pair Operations = 49 Triplet Operations = 343
n = 8, Pair Operations = 64 Triplet Operations = 512
n = 9, Pair Operations = 81 Triplet Operations = 729
n = 10, Pair Operations = 100 Triplet Operations = 1000
"""
