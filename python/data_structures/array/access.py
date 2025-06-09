"""Accessing elements in an array."""

array = [10, 20, 30, 40, 50]

# Accessing elements using positive indices
print("Positive Indexing:")
print("Element at index 0:", array[0])
print("Element at index 1:", array[1])

# Accessing elements using negative indices
print("\nNegative Indexing:")
print("Element at index -1 (last element):", array[-1])
print("Element at index -2 (second last element):", array[-2])

# Accessing elements using slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", array[1:4])
print("Elements from index 2 to end:", array[2:])
print("Elements from start to index 3:", array[:4])

# Accessing elements using step in slicing. 
# Add two colons to specify step
print("\nSlicing with step:")
print("Elements with step 2:", array[::2])

# Accessing elements using negative step in slicing
print("\nSlicing with negative step:")
print("Elements in reverse order:", array[::-2])

# Accessing elements using out-of-bounds indices
print("\nOut of Bounds Access:")
try:
    print("Element at index 5 (out of bounds):", array[5])  # This will raise an IndexError
except IndexError as exception:
    print("IndexError:", exception)

"""
Output:

Positive Indexing:
Element at index 0: 10
Element at index 1: 20

Negative Indexing:
Element at index -1 (last element): 50
Element at index -2 (second last element): 40

Slicing:
Elements from index 1 to 3: [20, 30, 40]
Elements from index 2 to end: [30, 40, 50]
Elements from start to index 3: [10, 20, 30, 40]

Slicing with step:
Elements with step 2: [10, 30, 50]

Slicing with negative step:
Elements in reverse order: [50, 30, 10]

Out of Bounds Access:
IndexError: list index out of range
"""