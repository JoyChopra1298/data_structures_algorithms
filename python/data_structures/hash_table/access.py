"""Accessing elements in a hash table."""

hash_table = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False
}

# Accessing elements using keys
name = hash_table['name']
age = hash_table['age']
city = hash_table['city']
is_student = hash_table['is_student']
print(f"Name: {name}, Age: {age}, City: {city}, Is Student: {is_student}")

# Accessing elements using the get() method
name_get = hash_table.get('name')
age_get = hash_table.get('age')
city_get = hash_table.get('city')
is_student_get = hash_table.get('is_student')
print(f"Using get(): Name: {name_get}, Age: {age_get}, City: {city_get}, Is Student: {is_student_get}")

# Accessing a non-existent key with get() method (returns None)
non_existent = hash_table.get('country')
print(f"Accessing non-existent key 'country': {non_existent}")

# Accessing a non-existent key with get() method (returns default value)
default_value = hash_table.get('country', 'USA')
print(f"Accessing non-existent key 'country' with default value: {default_value}")

# Accessing elements using keys with exception handling
try:
    non_existent_value = hash_table['country']
except KeyError:
    print("KeyError: 'country' key does not exist in the hash table.")

# Checking if a key exists in the hash table
if "country" in hash_table:
    print(hash_table["age"])  # Output: 30
else:
    print("Key country not found")

"""
Output:

Name: Alice, Age: 30, City: New York, Is Student: False
Using get(): Name: Alice, Age: 30, City: New York, Is Student: False
Accessing non-existent key 'country': None
Accessing non-existent key 'country' with default value: USA
KeyError: 'country' key does not exist in the hash table.
Key country not found
"""
