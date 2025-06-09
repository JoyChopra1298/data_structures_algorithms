"""
In Python, the built-in list type is a dynamic array that can grow and shrink in size.
It is heterogeneous, meaning it can store elements of different data types.
"""

"""Creating an array"""

# An array can be created using square brackets `[]` or the `list()` constructor.

# Example of creating an array using square brackets
array_using_square_brackets = [1, 2, 3, 4, 5]
print("Array created using square brackets:", array_using_square_brackets)

# Example of creating an array using the list() constructor
array_using_constructor = list((6, 7, 8, 9, 10))
print("List created using list() constructor:", array_using_constructor)

# Example of creating an empty array
empty_array = []
print("Empty array created:", empty_array)

# Example of creating an array of a specific size initialized with a default value.
array_size = 5
default_value = 0
array_with_size = [default_value] * array_size
print(f"Array of size {array_size} initialized with {default_value}:", array_with_size)

# Example of creating an array from string
string = "Hello, World!"
array_from_string = list(string)
print("Array created from string:", array_from_string)

# Example of creating a multidimensional array (list of lists)
rows = 3
columns = 4
multidimensional_array = [[0] * columns for _ in range(rows)]
print("Multidimensional array (3x4) initialized with 0s:")
for row in multidimensional_array:
    print(row)

# Example of creating array using list comprehension
array_comprehension = [x * 2 for x in range(5)]
print("Array created using list comprehension (doubles of 0 to 4):", array_comprehension)

# Example of heterogenous array
array_of_mixed_types = [1, "two", 3.0, True]
print("Array with mixed data types:", array_of_mixed_types)

"""
Output:

Array created using square brackets: [1, 2, 3, 4, 5]
List created using list() constructor: [6, 7, 8, 9, 10]
Empty array created: []
Array of size 5 initialized with 0: [0, 0, 0, 0, 0]
Array created from string: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
Multidimensional array (3x4) initialized with 0s:
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
Array created using list comprehension (doubles of 0 to 4): [0, 2, 4, 6, 8]
Array with mixed data types: [1, 'two', 3.0, True]
"""
