"""Grounds up implementation of a binary tree in Python."""

from enum import Enum


class StackNode:
    """Node class for stack used in DFS traversal."""
    
    def __init__(self, item):
        self.item = item  # Item stored in the node
        self.next = None  # Pointer to the next node in the stack

    def __str__(self):
        return f"StackNode with data {self.data}"
    
class Stack:
    """Stack class implemented using a singly linked list."""

    def __init__(self):
        self.top = None  # Top of the stack
        self.size = 0    # Size of the stack

    # Push operation takes O(1) time
    def push(self, data):
        """Push a new item onto the stack."""
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Pop operation takes O(1) time
    def pop(self):
        """Pop an item off the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_item = self.top.item
        self.top = self.top.next
        self.size -= 1
        return popped_item

    # Peek operation takes O(1) time
    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.item

    # Check if the stack is empty takes O(1) time
    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0

    # Get the size of the stack takes O(1) time
    def __len__(self):
        """Return the size of the stack."""
        return self.size
    

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


class BinaryTreeNode:

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
    
    def find_rightmost_leaf_descendant(self):
        current = self
        while not current.is_leaf_node():
            if current.right:
                current = current.right
            else:
                current = current.left
        return current
    
    def is_left_child(self):
        if not self.parent:
            return False
        left_child = self.parent.left
        if left_child == self:
            return True
        else:
            return False


class BinaryTree:

    # Create operation takes O(1) time
    def __init__(self):
        self.root = None
        self.size = 0

    # Insert operation takes O(n) time 
    def insert(self, data):
        new_node = BinaryTreeNode(data)
        
        # If the tree is empty, set the new node as root
        if self.is_empty():
            self.root = new_node
            self.size += 1
            return
        
        def insert_node(node):
            if not node.left:
                node.left = new_node
                new_node.parent = node
                self.size += 1
                return True
            elif not node.right:
                node.right = new_node
                new_node.parent = node
                self.size += 1
                return True
            return False

        self.bfs_traverse(insert_node) 

    # Delete operation takes O(n) time
    def delete(self, data):
        if self.is_empty():
            return "Tree is empty, cannot delete from it"
        
        found_node = self.search(data)
        
        if not found_node:
            return f"Node with value {data} could not be found."

        replacement_node = found_node.find_rightmost_leaf_descendant()

        # If the root node is to be deleted, we need to update root property 
        if found_node == self.root:
            self.root = replacement_node

        if replacement_node:
            # Step 1: Clear replacement node from it's old position
            replacement_parent = replacement_node.parent
            if replacement_parent:
                if replacement_node.is_left_child():
                    replacement_parent.left = None
                else:
                    replacement_parent.right = None

            # Step 2: Put replacement node instead of found node
            found_parent = found_node.parent
            found_left_child = found_node.left
            found_right_child = found_node.right

            if found_parent:
                if found_node.is_left_child():
                    found_parent.left = replacement_node
                else:
                    found_parent.right = replacement_node

            if found_left_child:
                found_left_child.parent = replacement_node
            if found_right_child:
                found_right_child.parent = replacement_node
            
            
            # Step 3: Copy all found node properties to replacement node
            replacement_node.left = found_node.left
            replacement_node.right = found_node.right
            replacement_node.parent = found_node.parent
        else:
            # Simply delete the found node
            # Since it has no children, it does not need to be replaced.
            found_parent = found_node.parent

            if found_parent:
                if found_node.is_left_child():
                    found_parent.left = None
                else:
                    found_parent.right = None

        print(f"Node with value {data} successfully deleted")
        self.size -= 1
        return True

    # Search operation takes O(n) time
    def search(self, data):
        if self.is_empty():
            return None
        
        found_node = None
        
        def search_node(node):
            """Function to search for a node in BFS traversal."""
            if node.data == data:
                return True
            return False
        
        found_node = self.bfs_traverse(func=search_node)
        return found_node if found_node else None

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    # Postorder traversal takes O(n) time
    def postorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        
        stack = Stack()
        # This will reverse the order to get post-order
        result_stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current = stack.pop()
            # Root gets pushed first in a stack, so it will be processed last
            result_stack.push(current)
            
            # Push left child first, so left subtree will be processed later in stack
            # and hence will be ahead in result stack
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            
        while not result_stack.is_empty():
            current = result_stack.pop()
            # Operate on the current node
            if func:
                should_stop_traversal = func(current)
                if should_stop_traversal:
                    return current
            else:
                print(current)

    # Preorder traversal takes O(n) time
    def preorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current = stack.pop()
            
            # Operate on the current node
            if func:
                should_stop_traversal = func(current)
                if should_stop_traversal:
                    return current
            else:
                print(current)
            
            # Push right child first, so left is processed first
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)

    # Inorder traversal takes O(n) time
    def inorder_traverse(self, func=None):
        # This is a type of depth-first traversal
        if self.is_empty():
            return
        
        stack = Stack()
        current = self.root

        while current or not stack.is_empty():
            while current:
                stack.push(current)
                current = current.left
            
            current = stack.pop()
            # Operate on the current node
            if func:
                should_stop_traversal = func(current)
                if should_stop_traversal:
                    return current
            else:
                print(current)

            current = current.right
    

    # BFS traversal takes O(n) time
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


# Example usage
binary_tree = BinaryTree()
print("Deleting from empty tree")
response = binary_tree.delete(1)  # Delete from empty tree
print(response)
binary_tree.insert(1)  # Insert root
binary_tree.insert(2)  # Insert left child of root
binary_tree.insert(3)  # Insert right child of root
binary_tree.insert(4)  # Insert left child of node with data 2

print("\nSearching for node with data 3:")
found_node = binary_tree.search(3)  # Search for a node with data 3
print(found_node if found_node else "Node not found")

binary_tree.insert(5)  # Insert right child of node with data 2
binary_tree.insert(6)  # Insert left child of node with data 3
binary_tree.insert(7)  # Insert right child of node with data 3
binary_tree.insert(8)  # Insert left child of node with data 4

print("\nDeleting more nodes:")
response = binary_tree.delete(9)  # Delete node which does not exist
print(response)
binary_tree.delete(1)  # Delete root node
binary_tree.delete(2)  # Delete another node

binary_tree.insert(9)
binary_tree.insert(10)
binary_tree.insert(11)

print("\nBFS Traversal of Binary Tree:")
binary_tree.bfs_traverse()

print("\nInorder Traversal of Binary Tree:")
binary_tree.inorder_traverse()
print("\n2nd time Inorder Traversal of Binary Tree:")
binary_tree.inorder_traverse()

print("\nPreorder Traversal of Binary Tree:")
binary_tree.preorder_traverse()

print("\nPostorder Traversal of Binary Tree:")
binary_tree.postorder_traverse()

"""
Output: 

Deleting from empty tree
Tree is empty, cannot delete from it

Searching for node with data 3:
Node with data 3

Deleting more nodes:
Node with value 9 could not be found.
Node with value 1 successfully deleted
Node with value 2 successfully deleted

BFS Traversal of Binary Tree:
Node with data 7
Node with data 5
Node with data 3
Node with data 4
Node with data 9
Node with data 6
Node with data 10
Node with data 8
Node with data 11

Inorder Traversal of Binary Tree:
Node with data 8
Node with data 4
Node with data 11
Node with data 5
Node with data 9
Node with data 7
Node with data 6
Node with data 3
Node with data 10

2nd time Inorder Traversal of Binary Tree:
Node with data 8
Node with data 4
Node with data 11
Node with data 5
Node with data 9
Node with data 7
Node with data 6
Node with data 3
Node with data 10

Preorder Traversal of Binary Tree:
Node with data 7
Node with data 5
Node with data 4
Node with data 8
Node with data 11
Node with data 9
Node with data 3
Node with data 6
Node with data 10

Postorder Traversal of Binary Tree:
Node with data 8
Node with data 11
Node with data 4
Node with data 9
Node with data 5
Node with data 6
Node with data 10
Node with data 3
Node with data 7
"""