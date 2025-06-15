"""Search value in a hash table."""

hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False
}

# Searching for value using values() method
for value in hash_table.values():
    if value == 'Alice':
        print(f"Found value: {value}")
        break
    else:
        print("Value not found")

"""
Output:

Found value: Alice
"""
