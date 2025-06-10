"""Grounds up implementation of an array in Python."""
import ctypes

class Array:

    # Array creation takes O(n) time 
    def __init__(self, capacity):
        self.capacity = capacity      # Maximum number of elements the array can hold
        self.size = 0                # Current number of elements in the array
        self.data = (capacity * ctypes.py_object)()  # Low-level array allocation

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])
    
    # Accessing elements takes O(1) time
    # Accessing using slice takes O(k) time, where k is the number of elements in the slice
    def __getitem__(self, index):
        if isinstance(index, slice):
            # Get start, stop, step from the slice object
            start, stop, step = index.indices(self.size)
            # Create a list with sliced elements
            return [self.data[i] for i in range(start, stop, step)]
        
        # Handle negative index
        if index < 0:
            index = self.size + index
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")
        
    # Updating an element takes O(1) time
    def __setitem__(self, index, value):
        if index < 0:
            index = self.size + index
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    
    # Array resizing takes O(n) time
    def _resize(self):
        """Resize the array to double its capacity."""
        new_capacity = self.capacity * 2
        new_data = (new_capacity * ctypes.py_object)()
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    # Append operation takes O(1) time on average, but can take O(n) if resizing is needed 
    def append(self, value):
        """Append a value to the end of the array."""
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    # Insert operation takes O(n) time in the worst case due to shifting elements and resizing if needed
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if self.size == self.capacity:
            self._resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    # Delete operation takes O(n) time in the worst case due to shifting elements
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

    # Search operation takes O(n) time
    def search(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i  # Return first matching index
        return -1  # Return -1 if the value is not found
    
    # Traversing the array takes O(n) time
    def traverse(self, func=None):
        if func is None:
            for i in range(self.size):
                print(self.data[i])
        else:
            for i in range(self.size):
                func(self.data[i])



array = Array(2)  # Create an array with a capacity of 2
print(f"Array: {array}. Current size: {array.size}, Capacity: {array.capacity}")

# Append elements to the array
array.append(10)
array.append(20)
print(f"Array after appending 10 and 20: {array}. Current size: {array.size}, Capacity: {array.capacity}")
array.append(30)  # This will trigger a resize
print(f"Array after appending 30 (resize should occur): {array}. Current size: {array.size}, Capacity: {array.capacity}")

print(f"Element at index 0: {array[0]}")
print(f"Element at index -2: {array[-2]}")
array.append(40)
print(f"Array after appending 40: {array}. Current size: {array.size}, Capacity: {array.capacity}")

# Accessing elements using slicing
print(f"Elements from index 1 to 3: {array[1:3]}")
# Accessing elements using step in slicing
print(f"Elements with step 2: {array[::2]}")

# Updating an element
array[1] = 99
print(f"Array after updating index 1 to 99: {array}. Current size: {array.size}, Capacity: {array.capacity}")

# Inserting an element at index 2
array.insert(2, 80)
print(f"Array after inserting 80 at index 2: {array}. Current size: {array.size}, Capacity: {array.capacity}")

# Deleting an element at index 0
array.delete(0)
print(f"Array after deleting element at index 0: {array}. Current size: {array.size}, Capacity: {array.capacity}")

# Searching for an element
index = array.search(80)
if index != -1:
    print(f"Element 80 found at index: {index}")
else:
    print("Element 80 not found in the array.")

# Traversing the array
print("Traversing the array:")
array.traverse()

# Using a custom function to traverse the array
print("Traversing the array with a custom function:")
def double_element(value):
    print(f"{value*2}")
array.traverse(double_element)
