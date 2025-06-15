# Hash Table

A hash table is a data structure that stores data in the form of key-value pairs. It provides efficient operations for inserting, accessing and deleting elements.

Hash table achieves fast data access using hash functions. Hash function computes an index from the key. This index determines the position where the value is stored. Hash function computation takes O(1) constant time.

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
| 1. | Access(key) | Access value for key | O(1) average, O(n) worst|
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

## Grounds up implementation 

| Number | Operation | Done | Time |
| -- | -- | -- | -- |
