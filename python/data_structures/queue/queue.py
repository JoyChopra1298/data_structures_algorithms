"""Grounds up implementation of a queue in Python."""

class Node:
    """Node class for queue."""

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the queue

    def __str__(self):
        return f"Node with data {self.data}"
    
class Queue:
    """Queue class implemented using a singly linked list."""

    def __init__(self):
        self.front = None  # Front of the queue
        self.rear = None   # Rear of the queue
        self.size = 0      # Size of the queue

    # Enqueue operation takes O(1) time
    def enqueue(self, data):
        """Add a new item to the end of the queue."""
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    # Dequeue operation takes O(1) time
    def dequeue(self):
        """Remove an item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue is now empty
            self.rear = None
        self.size -= 1
        return dequeued_data

    # Peek operation takes O(1) time
    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    # Check if the queue is empty takes O(1) time
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    # Get the size of the queue takes O(1) time
    def __len__(self):
        """Return the size of the queue."""
        return self.size
    

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.peek())  # Output: 10
print(queue.dequeue())  # Output: 10
queue.enqueue(30)
queue.enqueue(40)
print(queue.peek())  # Output: 20
print(len(queue))  # Output: 3
print(queue.is_empty())  # Output: False

"""
Output:

10
10
20
3
False
"""
