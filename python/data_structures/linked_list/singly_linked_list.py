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


    # String representation takes O(n) time, where n is the number of elements in the list
    def __str__(self):
        """String representation of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(map(str, elements))


linked_list = SinglyLinkedList()

# Example usage
linked_list.insert(0, 10)  # Insert at head
linked_list.insert(1, 20)  # Insert at tail
linked_list.insert(1, 15)  # Insert in the middle
print("Linked List after insertions:")
print(linked_list)  # Output: 10 -> 15 -> 20

