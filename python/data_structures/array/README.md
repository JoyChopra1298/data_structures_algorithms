# Array

An array is a collection of homogenous elements identified by their index. The elements are stored in contiguous memory locations. Each element in an array can be accessed directly using its index.

## Static vs Dynamic Arrays

**Static arrays** - The size of the array is fixed at initialisation. It cannot be changed later. Memory is allocated at compile time.

**Dynamic arrays** - The size of the array is managed by the system and can be increased or decreased as needed. Memory is allocated at runtime.

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Access(index) | Get element at index | O(1), O(k) for slicing |
| 2 | Update(index, x) | Update value at specific index | O(1) |
| 3 | Insert(index, x) | Insert element at index | O(n) |
| 4 | Append(x) | Add element at end | O(1) for static array, O(n) when resizing is needed |
| 5 | Delete(index) | Remove element at index | O(n) |
| 6 | Search(x) | Find element by value | O(n) |
| 7 | Traverse() | Visit all elements once | O(n) |
| 8 | Sort()| Rearrange elements in ascending or descending order | O(n.log(n))
| 9 | Resize(n2) | Modify size of the array | O(n), applicable only for dynamic arrays|

## Python built in operations 

| Number | Operation | Done |
| -- | -- | -- |
| 1 | Create array | &#9989; |
| 2 | Access array | &#9989; |
| 3 | Update array | &#9989; |
