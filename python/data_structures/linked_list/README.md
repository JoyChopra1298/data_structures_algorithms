# Linked List

A linked list is a linear data structure (forms a line) consisting of a sequence of nodes. Each node in the linked list contains 2 fields - 

1. Data field - Stores the actual data of the node
2. Reference field - Stores the reference of the next node in the sequence.

Memory for the nodes is allocated dynamically. The nodes are not stored contiguously like arrays.

* Head - The first node is called the head of the list
* Tail - The last node is called the tail of the list

## Types of linked lists

1. **Singly linked list** - Each node points to the next node
2. **Doubly linked list** - Each node points to both the previous and the next node
3. **Circular linked list** - The tail node points to head node thus forming a circle.

## Benefits of linked lists

1. **Dynamic size** - Can grow or shrink during runtime without needing a fixed size.
2. **Efficient insertions/deletions** - Unlike arrays, adding or removing nodes does not require shifting elements. This is specially helpful when each data element is of large size such that shifting them will consume large time.
3. **No memory waste** - Allocates memory only as needed. Unlike arrays which pre-allocate memory.
4. **Flexible memory usage** - Nodes can be scattered in memory. No requirement for contiguous blocks. So can work well with highly fragmented memory.
5. **Easy implementation for other data structures** - Stacks, Queues, Trees and Graphs

## Tips

When to use linked lists
1. Fast insertion
2. Fast deletion
3. Ordered
4. Flexible size

When not to use linked lists
1. Slow lookup - no random access - we have to traverse the list to access at an index
2. More memory

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Create() | Create an empty linked list | O(1) |
| 2 | Insert(index, value) | Insert value at index | O(n)* |
| 3 | Access(index) | Access value at index | O(n) |
| 4 | Update(index, value) | Update value at index | O(n) |
| 5 | Delete(index) | Delete node at index | O(n)* |
| 6 | Append(value) | Append value at the end | O(1) with tail pointer |
| 7 | Prepend(value) | Prepend value at the beginning | O(1) |
| 8 | Search(value) | Search value in the list | O(n) |
| 9 | Traverse() | Visit each node | O(n) |
| 10 | Sort() | Sort the linked list | O(n.logn) |

\* Practically faster than arrays because shifting of data elements is not required.

## Grounds up implementation 

| Number | Operation | Done | Time |
| -- | -- | -- | -- |
| 1 | Create new linked list | &#9989; | O(1) |
| 2 | Insert value at index | &#9989; | O(n) |
| 3 | Prepend value | &#9989; | O(1) |
| 4 | Append value | &#9989; | O(1) |
| 5 | Access value at index | &#9989; | O(n) |
| 6 | Update value at index | &#9989; | O(n) |
| 7 | Delete node at index | &#9989; | O(n) |
| 8 | Search value | &#9989; | O(n) |
| 9 | Traverse list | &#9989; | O(n) |
