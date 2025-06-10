"""Linear Search for an element in an array."""

array = [10, 20, 30, 40, 50]

value_to_find = 30

# Check for existence of the value in the array
found = value_to_find in array
if found:
    # Find the index of the value
    index = array.index(value_to_find)
    print(f"Value {value_to_find} found at index {index}.")
else:
    print(f"Value {value_to_find} not found in the array.")

# ValueError is thrown by index() method if the value is not found
value_to_find = 60  # This value does not exist in the array
try:
    index = array.index(value_to_find)
except ValueError:
    print(f"Value {value_to_find} not found in the array.")

"""
Output:

Value 30 found at index 2.
Value 60 not found in the array.
"""
