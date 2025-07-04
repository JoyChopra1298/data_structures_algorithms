"""Grounds up implementation of a binary search tree in Python."""

from enum import Enum


class QueueNode:
    """Node class for queue used in BFS traversal."""
    
    def __init__(self, item):
        self.item = item  # Item stored in the node
        self.next = None  # Pointer to the next node in the queue

    def __str__(self):
        return f"QueueNode with data {self.data}"
    
class Queue:
    """Queue class implemented using a linked list."""

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = QueueNode(item)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.front:
            raise IndexError("Dequeue from empty queue")
        dequeued_item = self.front.item
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return dequeued_item
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0


class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node
        self.parent = None  # Parent of the node

    def __str__(self):
        return f"Node with data {self.data}"
    
    def is_leaf_node(self):
        if self.left or self.right:
            return False
        return True
    
    def is_left_child(self):
        if not self.parent:
            return False
        left_child = self.parent.left
        if left_child == self:
            return True
        else:
            return False

class BinarySearchTree:

    # Create operation takes O(1) time
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def insert(self, value):
        new_node = BinarySearchTreeNode(value)

        if self.is_empty():
            self.root = new_node
            self.size += 1
            return
        
        current = self.root
        while True:
            current_value = current.data
            if value <= current_value:
                # Insert in left subtree
                if current.left:
                    current = current.left
                    continue
                else:
                    current.left = new_node
                    new_node.parent = current
                    self.size += 1
                    return
            else:
                # Insert in right subtree
                if current.right:
                    current = current.right
                    continue
                else:
                    current.right = new_node
                    new_node.parent = current
                    self.size += 1
                    return

    def delete(self, value):
        found_node = self.search(value)

        if not found_node:
            return f"Node with value {value} not found. Cannot delete."
        
        if found_node.left and found_node.right:
            replacement_node = self.get_rightmost_child_in_left_subtree(found_node)
            
            # Copy data from replacement node
            found_node.data = replacement_node.data
            
            # Delete replacement node
            replacement_node_parent = replacement_node.parent
            if replacement_node.is_left_child():
                replacement_node_parent.left = None
            else:
                replacement_node_parent.right = None

            self.size -= 1
            return True

        if found_node.is_leaf_node():
            # Found node is root
            if not found_node.parent:
                self.root = None
                self.size -= 1
                return True

            # Delete found node
            found_node_parent = found_node.parent
            if found_node.is_left_child():
                found_node_parent.left = None
            else:
                found_node_parent.right = None
            self.size -= 1
            return True
        
        # If only one child is there
        replacement_node = None
        if not found_node.left:
            replacement_node = found_node.right
        else:
            replacement_node = found_node.left

        if not found_node.parent:
            self.root = replacement_node
            replacement_node.parent = None
            self.size -= 1
            return True

        found_node_parent = found_node.parent
        if found_node.is_left_child():
            found_node_parent.left = replacement_node
        else:
            found_node_parent.right = replacement_node
        replacement_node.parent = found_node_parent
        self.size -= 1
        return True
        

    def get_rightmost_child_in_left_subtree(self, node):
        if not node.left:
            return None
        
        current = node.left
        while True:
            if current.right:
                current = current.right
            else:
                return current
        

    def search(self, value):
        if self.is_empty():
            return None
        
        current = self.root
        while True:
            current_data = current.data
            if current_data == value:
                return current
            elif value < current_data:
                if not current.left:
                    return None
                current = current.left
            else:
                if not current.right:
                    return None
                current = current.right


    def bfs_traverse(self, func=None):
        if self.is_empty():
            return

        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            current = queue.dequeue()
            
            # Operate on the current node
            if func:
                should_stop_traversal = func(current)
                if should_stop_traversal:
                    return current
            else:
                print(current)

            # Add children to the queue
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    def inorder_traverse_node(self, node, func):
        if node.left:
            self.inorder_traverse_node(node.left, func)
        
        # Operate on the current node
        if func:
            should_stop_traversal = func(node)
            if should_stop_traversal:
                return node
        else:
            print(node)

        if node.right:
            self.inorder_traverse_node(node.right, func)
            

    def inorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        self.inorder_traverse_node(self.root, func)

    def preorder_traverse_node(self, node, func):
        # Operate on the current node
        if func:
            should_stop_traversal = func(node)
            if should_stop_traversal:
                return node
        else:
            print(node)

        if node.left:
            self.preorder_traverse_node(node.left, func)

        if node.right:
            self.preorder_traverse_node(node.right, func)

    def preorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        self.preorder_traverse_node(self.root, func)

    def postorder_traverse_node(self, node, func):
        if node.left:
            self.postorder_traverse_node(node.left, func)

        if node.right:
            self.postorder_traverse_node(node.right, func)

        # Operate on the current node
        if func:
            should_stop_traversal = func(node)
            if should_stop_traversal:
                return node
        else:
            print(node)

    def postorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        self.postorder_traverse_node(self.root, func)


# Example usage
binary_search_tree = BinarySearchTree()
print("Deleting from empty tree")
response = binary_search_tree.delete(1)  # Delete from empty tree
print(response)
binary_search_tree.insert(4)  # Insert root
binary_search_tree.insert(2)  # Insert left child of root
binary_search_tree.insert(3)  # Insert right child of 2
binary_search_tree.insert(1)  # Insert left child of 2

print("\nSearching for node with data 3:")
found_node = binary_search_tree.search(3)  # Search for a node with data 3
print(found_node if found_node else "Node not found")

binary_search_tree.insert(8)  # Insert right child of root
binary_search_tree.insert(6)  # Insert left child of 8
binary_search_tree.insert(7)  # Insert right child of 6 
binary_search_tree.insert(5)  # Insert left child of 6

print("\nDeleting more nodes:")
response = binary_search_tree.delete(9)  # Delete node which does not exist
print(response)
binary_search_tree.delete(1)  # Delete root node
binary_search_tree.delete(2)  # Delete another node

binary_search_tree.insert(11)
binary_search_tree.insert(10)
binary_search_tree.insert(9)

print("\nBFS Traversal of Binary Tree:")
binary_search_tree.bfs_traverse()

print("\nInorder Traversal of Binary Tree:")
binary_search_tree.inorder_traverse()
print("\n2nd time Inorder Traversal of Binary Tree:")
binary_search_tree.inorder_traverse()

print("\nPreorder Traversal of Binary Tree:")
binary_search_tree.preorder_traverse()

print("\nPostorder Traversal of Binary Tree:")
binary_search_tree.postorder_traverse()
