"""Traversing an array in Python"""

array = [10, 20, 30, 40, 50]

# Using a for loop to traverse the array
print("Traversing the array using for loop:")
for value in array:
    print(value)

# Using index to traverse the array
print("\nTraversing the array using index:")
for index in range(len(array)):
    print(f"Index {index}: Value {array[index]}")

# Using enumerate to get index and value
print("\nTraversing the array using enumerate:")
for index, value in enumerate(array):
    print(f"Index {index}: Value {value}")

"""
Output:

Traversing the array using for loop:
10
20
30
40
50

Traversing the array using index:
Index 0: Value 10
Index 1: Value 20
Index 2: Value 30
Index 3: Value 40
Index 4: Value 50

Traversing the array using enumerate:
Index 0: Value 10
Index 1: Value 20
Index 2: Value 30
Index 3: Value 40
Index 4: Value 50
"""
