"""Deleting an element from a hash table."""

hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False
}

# Deleting a key-value pair using del
del hash_table['age']
print(f"Hash table after deleting 'age': {hash_table}")

# Deleting a key-value pair using pop.
# This allows you to specify a default value if the key does not exist.
removed_value = hash_table.pop('city', None)
print(f"Removed 'city': {removed_value}, Hash table after deletion: {hash_table}")

# Attempting to delete a non-existent key
removed_value = hash_table.pop('country', None)
print(f"Attempted to remove 'country': {removed_value}, Hash table remains unchanged: {hash_table}")

# Deleting last inserted key-value pair using popitem
removed_item = hash_table.popitem()
print(f"Removed last inserted item: {removed_item}, Hash table after popitem: {hash_table}")

# Clearing the entire hash table
hash_table.clear()
print(f"Hash table after clearing: {hash_table}")

"""
Output:

Hash table after deleting 'age': {'name': 'Alice', 'city': 'New York', 'is_student': False}
Removed 'city': New York, Hash table after deletion: {'name': 'Alice', 'is_student': False}
Attempted to remove 'country': None, Hash table remains unchanged: {'name': 'Alice', 'is_student': False}
Removed last inserted item: ('is_student', False), Hash table after popitem: {'name': 'Alice'}
Hash table after clearing: {}
"""
