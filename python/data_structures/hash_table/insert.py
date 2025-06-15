"""Inserting an element in a hash table."""

# Creating a hash table
hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Inserting a new key-value pair
new_key = 'is_student'
new_value = True
hash_table[new_key] = new_value
print(f"Hash table after inserting '{new_key}': {hash_table}")

# Inserting multiple key-value pairs
new_entries = {
    'country': 'USA',
    'hobby': 'Reading'
}
hash_table.update(new_entries)
print(f"Hash table after inserting multiple entries: {hash_table}")

"""
Output:

Hash table after inserting 'is_student': {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_student': True}
Hash table after inserting multiple entries: {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_student': True, 'country': 'USA', 'hobby': 'Reading'}
"""
