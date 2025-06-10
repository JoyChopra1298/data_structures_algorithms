"""Sort an array"""

array = [410, 280, 130, 400, 50]

# Sorting in place
array.sort()
print(f"Sorted array: {array}")

array = [410, 280, 130, 400, 50]
# Sorting in reverse order
array.sort(reverse=True)
print(f"Sorted array in reverse order: {array}")

array = [410, 280, 130, 400, 50]
# Using sorted() to return a new sorted array
sorted_array = sorted(array)
print(f"Original array: {array}")
print(f"Sorted array using sorted(): {sorted_array}")

string_array = ["banana", "apple", "cherry", "date"]
# Sorting an array of strings using custom function which is applied to each element(key)
string_array.sort(key=lambda x: len(x))
print(f"Sorted string array by length: {string_array}")

"""
Output:

Sorted array: [50, 130, 280, 400, 410]
Sorted array in reverse order: [410, 400, 280, 130, 50]
Original array: [410, 280, 130, 400, 50]
Sorted array using sorted(): [50, 130, 280, 400, 410]
Sorted string array by length: ['date', 'apple', 'banana', 'cherry']
"""
