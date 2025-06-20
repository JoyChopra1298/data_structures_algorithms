# Queue

A queue is a linear data structure that follows First In First Out (FIFO) principle. This means the first element added to the queue is the first element to be removed.

## Use cases

1. CPU process scheduling
2. Handling requests in web servers
3. BFS in graphs and trees
4. Callback queues in event-driven programming

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Enqueue(value) | Add value to the end of the queue | O(1) |
| 2 | Dequeue() | Remove and return the first value from the queue | O(1) |
| 3 | Peek()/Front() | Return the first value without removing it | O(1) |
| 4 | isEmpty() | Check if the queue is empty | O(1) |
| 5 | size() | Return the number of items in the queue | O(1) if size is maintained as a property else O(n) |

## Grounds up implementation 

Same as above. Create takes O(1) time
