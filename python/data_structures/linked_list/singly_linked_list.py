"""Grounds up implementation of a singly linked list in Python."""

class Node:
    """Node class for singly linked list."""

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the list

class SinglyLinkedList:
    """Singly linked list class."""

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

        if current.next.next is None:
            current.next = None
            self.tail = current
        else:
            current.next = current.next.next
        self.size -= 1


    # String representation takes O(n) time, where n is the number of elements in the list
    def __str__(self):
        """String representation of the linked list."""
        elements = []
        structure = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        structure.append("Head: " + str(self.head.data) if self.head else "Head: None")
        structure.append("Tail: " + str(self.tail.data) if self.tail else "Tail: None")
        structure.append("Size: " + str(self.size))
        return " -> ".join(map(str, elements)) + "\n" + ", ".join(structure)


linked_list = SinglyLinkedList()

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
