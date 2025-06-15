"""Traversing a hash table."""

hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False
}

# Traversing the hash table using a for loop
print("Traversing the hash table using a for loop:")
for key in hash_table:
    print(f"Key: {key}, Value: {hash_table[key]}")

# Traversing the hash table using items() method
print("\nTraversing the hash table using items() method:")
for key, value in hash_table.items():
    print(f"Key: {key}, Value: {value}")

# Traversing the hash table using keys() method
print("\nTraversing the hash table using keys() method:")
for key in hash_table.keys():
    print(f"Key: {key}")

# Traversing the hash table using values() method
print("\nTraversing the hash table using values() method:")
for value in hash_table.values():
    print(f"Value: {value}")

# Using enumerate to get index and value
# Enumerate adds an index to the iterator that is passed to it.
print("\nTraversing the hash table with index using enumerate:")
for index, (key, value) in enumerate(hash_table.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

"""
Output:

Traversing the hash table using a for loop:
Key: name, Value: Alice
Key: age, Value: 30
Key: city, Value: New York
Key: is_student, Value: False

Traversing the hash table using items() method:
Key: name, Value: Alice
Key: age, Value: 30
Key: city, Value: New York
Key: is_student, Value: False

Traversing the hash table using keys() method:
Key: name
Key: age
Key: city
Key: is_student

Traversing the hash table using values() method:
Value: Alice
Value: 30
Value: New York
Value: False

Traversing the hash table with index using enumerate:
Index: 0, Key: name, Value: Alice
Index: 1, Key: age, Value: 30
Index: 2, Key: city, Value: New York
Index: 3, Key: is_student, Value: False
"""
