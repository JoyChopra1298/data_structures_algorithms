"""Grounds up implementation of a doubly linked list in Python."""

class Node:
    """Node class for doubly linked list."""

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

    def __str__(self):
        return f"Node with data {self.data}"

class DoublyLinkedList:
    """Doubly linked list class."""

    # Creating a singly linked list takes O(1) time
    def __init__(self):
        self.head = None  # Head of the list
        self.tail = None  # Tail of the list
        self.size = 0     # Size of the list

    # Inserting a new node takes O(n) time
    def insert(self, index, data):
        """Insert a new node with data at the specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    # Prepend operation takes O(1) time
    def prepend(self, data):
        """Insert a new node with data at the head of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # Append operation takes O(1) time
    def append(self, data):
        """Insert a new node with data at the tail of the list."""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Get operation takes O(n) time in the worst case
    def get(self, index):
        """Retrieve the data at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head

        if index == self.size - 1:
            return self.tail.data

        for _ in range(index):
            current = current.next
        return current.data
    
    # Update operation takes O(n) time in the worst case
    def update(self, index, data):
        """Update the data at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == self.size - 1:
            self.tail.data = data
            return
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    # Delete operation takes O(n) time in the worst case
    def delete(self, index):
        """Delete the node at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head

        for _ in range(index - 1):
            current = current.next

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        
        if index == 0:
            self.head = current.next
            self.head.prev = None

        if current.next.next is None:
            current.next = None
            self.tail = current
        else:
            current.next.next.prev = current
            current.next = current.next.next
        self.size -= 1

    # Search operation takes O(n) time
    def search(self, data):
        """Search for a value in the list"""
        current = self.head
        while(current): 
            if (data == current.data):
                return current
            else:
                current = current.next
        return None
    
    def traverse(self, func=None):
        """
        Traverse the linked list and apply function at each node.
        Print element if no function is specified
        """
        current = self.head

        while(current):
            if func:
                func(current.data)
            else:
                print(current.data)
            current = current.next


    # String representation takes O(n) time, where n is the number of elements in the list
    def __str__(self):
        """String representation of the linked list."""
        elements = []
        structure = []
        reverse = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        structure.append("Head: " + str(self.head.data) if self.head else "Head: None")
        structure.append("Tail: " + str(self.tail.data) if self.tail else "Tail: None")
        structure.append("Size: " + str(self.size))

        current = self.tail
        while current:
            reverse.append(current.data)
            current = current.prev

        return (" -> ".join(map(str, elements)) + "\n" + 
                ", ".join(structure) + "\n" + " <- ".join(map(str, reverse)))


linked_list = DoublyLinkedList()

# Example usage
linked_list.insert(0, 10)  # Insert at head
linked_list.insert(1, 20)  # Insert at tail
linked_list.insert(1, 15)  # Insert in the middle
print("Linked List after insertions:")
print(linked_list)  # Output: 10 -> 15 -> 20

linked_list.prepend(5)  # Prepend at head
linked_list.append(25)  # Append at tail
print("\nLinked List after prepend and append:")
print(linked_list)  # Output: 5 -> 10 -> 15 -> 20 -> 25

# Get elements by index
print("\nElement at index 0:", linked_list.get(0))  # Output: 5
print("Element at index 2:", linked_list.get(2))  # Output: 15
print("Element at index 4:", linked_list.get(4))  # Output: 25

# Update elements by index
linked_list.update(0, 1)  # Update head
linked_list.update(2, 16)  # Update middle element
linked_list.update(4, 30)  # Update tail
print("\nLinked List after updates:")
print(linked_list)  # Output: 1 -> 10 -> 16 -> 20 -> 30

# Search elements by value
print("\nSearching elements")
print(f"Node for value 1: {linked_list.search(1)}")
print(f"Node for value 16: {linked_list.search(16)}")
print(f"Node for value 30: {linked_list.search(30)}")
print(f"Node for value 19: {linked_list.search(19)}")

# Traverse the linked list
print("\nTraversing the linked list:")
linked_list.traverse()

def double(value):
    print(2 * value)

print("\nTraversing the linked list with double function:")
linked_list.traverse(double)

# Delete elements by index
linked_list.delete(0)  # Delete head
linked_list.delete(3)  # Delete tail
linked_list.delete(1)  # Delete middle element
print("\nLinked List after deletions:")
print(linked_list)  # Output: 10 -> 20

# Delete the last remaining elements
linked_list.delete(0)  # Delete head
linked_list.delete(0)  # Delete head
print("\nLinked List after deleting all elements:")
print(linked_list)  # Output: Head: None, Tail: None
# The linked list is now empty

"""
Output:

Linked List after insertions:
10 -> 15 -> 20
Head: 10, Tail: 20, Size: 3
20 <- 15 <- 10

Linked List after prepend and append:
5 -> 10 -> 15 -> 20 -> 25
Head: 5, Tail: 25, Size: 5
25 <- 20 <- 15 <- 10 <- 5

Element at index 0: 5
Element at index 2: 15
Element at index 4: 25

Linked List after updates:
1 -> 10 -> 16 -> 20 -> 30
Head: 1, Tail: 30, Size: 5
30 <- 20 <- 16 <- 10 <- 1

Searching elements
Node for value 1: Node with data 1
Node for value 16: Node with data 16
Node for value 30: Node with data 30
Node for value 19: None

Traversing the linked list:
1
10
16
20
30

Traversing the linked list with double function:
2
20
32
40
60

Linked List after deletions:
10 -> 20
Head: 10, Tail: 20, Size: 2
20 <- 10

Linked List after deleting all elements:

Head: None, Tail: None, Size: 0
"""
