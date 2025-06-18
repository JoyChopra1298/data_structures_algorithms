# Hash Table

A hash table is a data structure that stores data in the form of key-value pairs. It provides efficient operations for inserting, accessing and deleting elements.

## Hash functions

Hash table achieves fast data access using hash functions. Hash function computes an index from the key. This index determines the position where the value is stored. Hash function computation takes O(1) constant time.

Properties of a good hash function
1. **Deterministic** - Produces same hash value for same input key
2. **Uniform** - Evenly distributes keys to reduce collisions
3. **Fast Computation** - Ideally it should compute in constant time for each key. O(1)
4. **Avalanche effect** - Small changes in input drastically change the output hash value, improving distribution.

## Collisions

If 2 keys map to the same position by the hash function, then collision occurs. It can be solved using chaining or probing.

1. **Chaining** - Chaining handles collisions by storing all values at an index in a linked list at that index.

2. **Probing** - Probing resolves collisions by finding another open slot in the hash table array


## Tips

When to use hash tables
1. Fast lookups
2. Fast inserts
3. Fast deletes
4. Flexible keys

When not to use hash tables
1. Unordered
2. Slow key iteration

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Access(key) | Access value for key | O(1) average, O(n) worst|
| 2 | Update(key, x) | Update value at specific key | O(1) average, O(n) worst |
| 3 | Insert(key, x) | Insert value at key | O(1) average, O(n) worst |
| 4 | Delete(key) | Remove value at key | O(1) average, O(n) worst |
| 5 | Traverse() | Visit all key-value pairs once | O(m) ~ O(n)*|
| 6 | Keys() | Return list of all keys | O(m) ~ O(n)*|
| 7 | Values() | Return list of all values | O(m) ~ O(n)*|
| 8 | Entries() | Return list of all key-value pairs | O(m) ~ O(n)*|

\* where m is number of buckets allocated for the hash table. Practically m is proportional to n, n ~ .7*m so O(n)


## Python built in operations 

| Number | Operation | Done |
| -- | -- | -- |
| 1 | Create new hash table | &#9989; |
| 2 | Access key in hash table | &#9989; |
| 3 | Update value at key in hash table | &#9989; |
| 4 | Insert value at key in hash table | &#9989; |
| 5 | Delete value at key in hash table | &#9989; |
| 6 | Traverse key-value pairs of hash table | &#9989; |
| 7 | Traverse keys of hash table | &#9989; |
| 8 | Traverse values of hash table | &#9989; |
| 9 | Search value in hash table | &#9989; |

## Grounds up implementation 

| Number | Operation | Done | Time |
| -- | -- | -- | -- |
| 1 | Create new hash table | &#9989; | O(n), where n is the capacity of the hash table |
| 2 | Access key in hash table | &#9989; | O(1) average, O(n) worst | 
| 3 | Resize hash table | &#9989; | O(n) | 
| 4 | Insert value at key in hash table | &#9989; | O(1) average, O(n) worst | 
| 5 | Update value at key in hash table | &#9989; | O(1) average, O(n) worst | 
| 6 | Delete key in hash table | &#9989; | O(1) average, O(n) worst | 
| 7 | Traverse key-value pairs of hash table | &#9989; | O(n) | 
| 8 | Traverse keys of hash table | &#9989; | O(n) | 
| 9 | Traverse values of hash table | &#9989; | O(n) | 
| 10 | Search value in hash table | &#9989; | O(n) | 
