# Array

An array is a collection of homogenous elements identified by their index. The elements are stored in contiguous memory locations. Each element in an array can be accessed directly using its index.

## Static vs Dynamic Arrays

**Static arrays** - The size of the array is fixed at initialisation. It cannot be changed later. Memory is allocated at compile time.

**Dynamic arrays** - The size of the array is managed by the system and can be increased or decreased as needed. Memory is allocated at runtime.

## Operations

| Operation | Description | Time Complexity |
| -- | -- | -- |
| Access(index) | Get element at index | O(1) |
| Update(index, x) | Update value at specific index | O(1) |
| Insert(index, x) | Insert element at index | O(n) |
| Append(x) | Add element at end | O(1) for static array, O(n) when resizing is needed |
| Delete(index) | Remove element at index | O(n) |
| Search(x) | Find element by value | O(n) |
| Traverse() | Visit all elements once | O(n) |
| Sort()| Rearrange elements in ascending or descending order | O(n.log(n))
| Resize(n2) | Modify size of the array | O(n), applicable only for dynamic arrays|

## Python built in operations 

| Operation | Done |
| -- | -- |
| Create array | &#9989; |
