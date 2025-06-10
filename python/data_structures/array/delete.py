"""Deleting an element from an array."""

array = [10, 20, 30, 40, 50]

# Deleting an element at a specific index
index_to_delete = 2
del array[index_to_delete]
print(f"Array after deleting element at index {index_to_delete}: {array}")

"""
Output:

Array after deleting element at index 2: [10, 20, 40, 50]
"""