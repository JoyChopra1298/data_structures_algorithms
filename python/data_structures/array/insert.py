"""Inserting an element in an array at a given index."""

array = [10, 20, 30, 40, 50]

# Inserting an element at a specific index
index_to_insert = 2
new_value = 99

array.insert(index_to_insert, new_value)
print(f"Array after inserting {new_value} at index {index_to_insert}: {array}")

"""
Output:

Array after inserting 99 at index 2: [10, 20, 99, 30, 40, 50]
"""
