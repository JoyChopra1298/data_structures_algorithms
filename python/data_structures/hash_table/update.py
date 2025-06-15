"""Updating a value in a hash table."""

hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False
}

# Updating an existing key
hash_table['age'] = 31
print(f"Updated age: {hash_table['age']}")

# Updating multiple keys
hash_table.update({
    'city': 'Los Angeles',
    'is_student': True
})
print(f"Updated city: {hash_table['city']}, Is Student: {hash_table['is_student']}")

"""
Output:

Updated age: 31
Updated city: Los Angeles, Is Student: True
"""
