"""Grounds Up Implementation of a Hash Table in Python"""


class HashTable:

    # Creating a hash table takes O(n) time, where n is the initial capacity
    # TIP - Use prime number for initial capacity to reduce collisions
    def __init__(self, capacity=11):
        self.capacity = capacity  # Initial capacity of the hash table
        self.size = 0             # Current number of elements in the hash table

        # Initialize the hash table with empty lists
        # Each index in the table will hold a list to handle collisions using chaining
        self.table = [[] for _ in range(capacity)]  

    # Hash function computation takes O(1) time
    def _hash(self, key):
        """Hash function to compute the index for a given key."""
        # Python provides a built-in hash function that can be used to compute 
        # the hash value of any data type like strings, integers, tuples.
        return hash(key) % self.capacity

    # Inserting a key-value pair takes O(1) on average, O(n) in the worst case due to collisions
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists in the bucket
        # If it exists, update the value; if not, append the new key-value pair
        # Note this loop is only for the bucket at the computed index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))  # Insert new key-value pair
        self.size += 1

    # Updating a value by key takes O(1) on average, O(n) in the worst case due to collisions
    def update(self, key, value):
        """Update the value of an existing key in the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If the key does not exist, raise an error
        raise KeyError(f"Key '{key}' not found in the hash table.")

    # Retrieving a value by key takes O(1) on average, O(n) in the worst case due to collisions
    def get(self, key):
        """Retrieve a value by its key from the hash table."""
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None  # Key not found
    
    # Resizing the hash table takes O(n) time, where n is the number of elements in the table
    # This is due to rehashing all existing key-value pairs into the new table
    def resize(self):
        """Resize the hash table to double its capacity."""
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]
        
        for bucket in old_table:
            if bucket is not None:
                # This is done to rehash all existing key-value pairs
                # into the new table with the updated capacity
                for key, value in bucket:
                    self.insert(key, value)

    # Deleting a key-value pair takes O(1) on average, O(n) in the worst case due to collisions
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    self.size -= 1
                    return True
        return False  # Key not found

    """
    String representation takes O(n) time, where n is the number of elements in the table
    This is due to iterating through all buckets and their items.
    """
    def __str__(self):
        """String representation of the hash table."""
        items = []
        for bucket in self.table:
            if bucket is not None:
                items.append(bucket)
        return str(items)
    
    # Takes O(n) time, where n is the number of elements in the table
    def entries(self):
        """Return all key-value pairs in the hash table."""
        entries = []
        for bucket in self.table:
            if bucket is not None:
                entries.extend(bucket)
        return entries
    
    # Takes O(n) time, where n is the number of elements in the table
    def keys(self):
        """Return all keys in the hash table."""
        keys = []
        for bucket in self.table:
            if bucket is not None:
                keys.extend([k for k, v in bucket])
        return keys
    
    # Takes O(n) time, where n is the number of elements in the table
    def values(self):
        """Return all values in the hash table."""
        values = []
        for bucket in self.table:
            if bucket is not None:
                values.extend([v for k, v in bucket])
        return values
    
    # Takes O(n) time, where n is the number of elements in the table
    def search(self, value):
        """Search for a value in the hash table and return its key."""
        for bucket in self.table:
            if bucket is not None:
                for k, v in bucket:
                    if v == value:
                        return k
        return None  # Value not found
    
    
"""Example usage of the HashTable class:"""

hash_table = HashTable(3)
hash_table.insert('name', 'Alice')
hash_table.insert('age', 30)
hash_table.insert('city', 'New York')
hash_table.insert('is_student', False)
print("Hash Table after insertions:")
print(hash_table)

hash_table.resize()  # Resize the hash table

print("\nHash Table after resizing:")
print(hash_table)
hash_table.insert('country', 'USA')
hash_table.insert('hobby', 'Reading')
print("\nHash Table after inserting more elements:")
print(hash_table)

print("\nRetrieving 'name':", hash_table.get('name'))
print("Retrieving 'age':", hash_table.get('age'))
print("Retrieving 'non_existent':", hash_table.get('non_existent'))

hash_table.update('age', 31)
print("\nHash Table after updating 'age':")
print(hash_table)

hash_table.delete('city')
print("\nHash Table after deleting 'city':")
print(hash_table)

print("\nAll entries in the hash table:")
print(hash_table.entries())

print("\nAll keys in the hash table:")
print(hash_table.keys())

print("\nAll values in the hash table:")
print(hash_table.values())

print("\nSearching for value 'USA':", hash_table.search('USA'))
print("Searching for value 'NonExistent':", hash_table.search('NonExistent'))

"""
Output:

Hash Table after insertions:
[[('is_student', False)], [('name', 'Alice'), ('age', 30)], [('city', 'New York')]]

Hash Table after resizing:
[[], [], [], [('is_student', False)], [('name', 'Alice'), ('age', 30)], [('city', 'New York')]]

Hash Table after inserting more elements:
[[], [], [('country', 'USA'), ('hobby', 'Reading')], [('is_student', False)], [('name', 'Alice'), ('age', 30)], [('city', 'New York')]]

Retrieving 'name': Alice
Retrieving 'age': 30
Retrieving 'non_existent': None

Hash Table after updating 'age':
[[], [], [('country', 'USA'), ('hobby', 'Reading')], [('is_student', False)], [('name', 'Alice'), ('age', 31)], [('city', 'New York')]]

Hash Table after deleting 'city':
[[], [], [('country', 'USA'), ('hobby', 'Reading')], [('is_student', False)], [('name', 'Alice'), ('age', 31)], []]

All entries in the hash table:
[('country', 'USA'), ('hobby', 'Reading'), ('is_student', False), ('name', 'Alice'), ('age', 31)]

All keys in the hash table:
['country', 'hobby', 'is_student', 'name', 'age']

All values in the hash table:
['USA', 'Reading', False, 'Alice', 31]

Searching for value 'USA': country
Searching for value 'NonExistent': None
"""
