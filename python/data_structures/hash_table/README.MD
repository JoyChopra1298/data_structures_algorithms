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

## Python built in operations 

| Number | Operation | Done |
| -- | -- | -- |

## Grounds up implementation 

| Number | Operation | Done | Time |
| -- | -- | -- | -- |
