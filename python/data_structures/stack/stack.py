"""Grounds up implementation of a stack in Python."""

class Node:
    """Node class for stack."""

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the stack

    def __str__(self):
        return f"Node with data {self.data}"
    

class Stack:
    """Stack class implemented using a singly linked list."""

    def __init__(self):
        self.top = None  # Top of the stack
        self.size = 0    # Size of the stack

    # Push operation takes O(1) time
    def push(self, data):
        """Push a new item onto the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Pop operation takes O(1) time
    def pop(self):
        """Pop an item off the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0

    def __len__(self):
        """Return the size of the stack."""
        return self.size
    

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(len(stack))    # Output: 1
stack.push(30)
stack.push(40)
print(stack.peek())  # Output: 40
print(stack.is_empty())  # Output: False

"""
Output:

20
20
1
40
False
"""