"""
In Python, the built-in dict type is a hash table.
"""

"""Creating an hash table"""

# An hash table can be created using curly braces `{}` or the `dict()` constructor.

# Example of creating a hash table using curly braces
hash_table_using_curly_braces = {'key1': 'value1', 'key2': 'value2'}
print("Hash table created using curly braces:", hash_table_using_curly_braces)

# Example of creating a hash table using the dict() constructor
hash_table_using_constructor = dict(key3='value3', key4='value4')
print("Hash table created using dict() constructor:", hash_table_using_constructor)

# Example of creating an empty hash table
empty_hash_table = {}
print("Empty hash table created:", empty_hash_table)

"""
Output:

Hash table created using curly braces: {'key1': 'value1', 'key2': 'value2'}
Hash table created using dict() constructor: {'key3': 'value3', 'key4': 'value4'}
Empty hash table created: {}
"""