# Stack

A stack is a linear data structure that follows Last in First Out (LIFO) principle. This means that the last element added onto the stack is the first element to be removed.

## Use cases

1. Call stack for function call management in programming languages
2. Undo mechanism in text editors
3. Browser history navigation
4. Backtracking algorithms
5. Expression evaluation and syntax parsing

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Push(value) | Add value to the top of the stack | O(1) |
| 2 | Pop() | Remove and return the top value from the stack | O(1) |
| 3 | Peek()/Top() | Return the top value without removing it | O(1) |
| 4 | isEmpty() | Check if the stack is empty | O(1) |
| 5 | size() | Return the number of items in the stack | O(1) if size is maintained as a property else O(n) |

## Grounds up implementation 

Same as above. Create takes O(1) time
