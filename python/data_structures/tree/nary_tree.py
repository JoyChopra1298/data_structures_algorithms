"""Grounds up implementation of an N-ary tree in Python."""

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

class TreeNode:
    """Node class for N-ary tree."""

    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.children = None # Pointer to the first child node
        self.next = None # Pointer to the right sibling node
        self.previous = None # Pointer to the left sibling node
        self.parent = None  # Pointer to the parent node
        self.num_children = 0 # Number of children this node has

    def get_last_child(self):
        """Get the last child node."""
        if not self.children:
            return None
        current = self.children
        while current.next:
            current = current.next
        return current
    
    def get_rightmost_leaf(self):
        """Get the rightmost leaf node."""
        if not self.children:
            return None
        current = self.children
        while current.next:
            current = current.next
        if current.num_children > 0:
            return current.get_rightmost_leaf()
        else:
            return current

    def __str__(self):
        return f"Node with data {self.data} and {self.num_children} children"
    
class NaryTree:
    """N-ary tree class implemented using a linked list."""
    
    # Create operation takes O(1) time
    def __init__(self, max_children):
        self.root = None  # Root of the N-ary tree
        self.size = 0     # Size of the N-ary tree
        self.max_children = max_children

    # Insert operation takes O(n) time in the worst case
    def insert(self, data):
        """Insert a new node into the N-ary tree."""
        new_node = TreeNode(data)

        # If the tree is empty, set the new node as root
        if self.is_empty():
            self.root = new_node
            self.size += 1
            return
        
        def insert_node(node):
            """Function to insert a node in BFS traversal."""
            if node.num_children < self.max_children:
                # Insert the new node as a child of the current node
                if not node.children:
                    node.children = new_node
                else:
                    child = node.get_last_child()
                    child.next = new_node
                    new_node.previous = child
                new_node.parent = node
                node.num_children += 1
                return True
            return False
        
        self.bfs_traverse(func=insert_node)
        self.size += 1

    # Search operation takes O(n) time
    def search(self, data):
        """Search for a node in the N-ary tree."""
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

    # Deleting a node takes O(n) time
    def delete(self, data):
        """Delete a node from the N-ary tree."""
        
        if self.is_empty():
            return "Tree is empty, cannot delete from it"
        
        found_node = self.search(data)
        
        if not found_node:
            return f"Node with value {data} could not be found."

        replacement_node = found_node.get_rightmost_leaf()

        # If the root node is to be deleted, we need to update root property 
        if found_node == self.root:
            self.root = replacement_node

        if replacement_node:
            # Step 1: Clear replacement node from it's old position
            # We do not have to worry about next and children properties since 
            # replacement node is the rightmost leaf
            replacement_left_sibling = replacement_node.previous
            replacement_parent = replacement_node.parent

            # If replacement node has left sibling
            if replacement_left_sibling:
                replacement_left_sibling.next = None
                replacement_parent.num_children -= 1
            # If replacement node is the only child
            elif replacement_parent:
                replacement_parent.children = None
                replacement_node.num_children = 0

            # Step 2: Put replacement node instead of found node
            found_left_sibling = found_node.previous
            found_right_sibling = found_node.next
            found_parent = found_node.parent
            found_children = found_node.children

            if found_left_sibling:
                found_left_sibling.next = replacement_node
            elif found_parent:
                found_parent.children = replacement_node
            if found_right_sibling:
                found_right_sibling.previous = replacement_node
            if found_children:
              current_child = found_children
              while current_child:
                  current_child.parent = replacement_node
                  current_child = current_child.next  
            
            # Step 3: Copy all found node properties to replacement node
            replacement_node.previous = found_node.previous
            replacement_node.parent = found_node.parent
            replacement_node.children = found_node.children
            replacement_node.next = found_node.next
            replacement_node.num_children = found_node.num_children

        else:
            # Simply delete the found node
            # Since it has no children, it does not need to be replaced.
            found_left_sibling = found_node.previous
            found_right_sibling = found_node.next
            found_parent = found_node.parent

            # If left sibling exists, update it
            if found_left_sibling:
                found_left_sibling.next = found_right_sibling
                found_parent.num_children -= 1
            # Otherwise found_node is the only child
            elif found_parent:
                found_parent.children = None
                found_parent.num_children = 0

        print(f"Node with value {data} successfully deleted")
        self.size -= 1
        return True
        

    # BFS traversal takes O(n) time
    def bfs_traverse(self, func=None):
        """Breadth-first traversal of the N-ary tree."""
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
            child = current.children
            while child:
                queue.enqueue(child)
                child = child.next

    # Check if the N-ary tree is empty takes O(1) time
    def is_empty(self):
        """Check if the N-ary tree is empty."""
        return self.size == 0
    
    def __len__(self):
        """Return the size of the N-ary tree."""
        return self.size
    
# Example usage
nary_tree = NaryTree(max_children=5)
print("Deleting from empty tree")
response = nary_tree.delete(1)  # Delete from empty tree
print(response)
nary_tree.insert(1)  # Insert root
nary_tree.insert(2)  # Insert child of root
nary_tree.insert(3)  # Insert another child of root
nary_tree.insert(4)  # Insert another child of root

print("\nSearching for node with data 3:")
found_node = nary_tree.search(3)  # Search for a node with data 3
print(found_node if found_node else "Node not found")

nary_tree.insert(5)  # Insert another child of root
nary_tree.insert(6)  # Insert another child of root
nary_tree.insert(7)  # Insert child of node with data 2
nary_tree.insert(8)  # Insert another child of node with data 2

print("\nDeleting more nodes:")
response = nary_tree.delete(9)  # Delete node which does not exist
print(response)
nary_tree.delete(1)  # Delete root node
nary_tree.delete(2)  # Delete another node

nary_tree.insert(9)
nary_tree.insert(10)
nary_tree.insert(11)

print("\nBFS Traversal of N-ary Tree:")
nary_tree.bfs_traverse()

"""
Output:

Deleting from empty tree
Tree is empty, cannot delete from it

Searching for node with data 3:
Node with data 3 and 0 children

Deleting more nodes:
Node with value 9 could not be found.
Node with value 1 successfully deleted
Node with value 2 successfully deleted

BFS Traversal of N-ary Tree:
Node with data 6 and 5 children
Node with data 8 and 3 children
Node with data 3 and 0 children
Node with data 4 and 0 children
Node with data 5 and 0 children
Node with data 9 and 0 children
Node with data 7 and 0 children
Node with data 10 and 0 children
Node with data 11 and 0 children
"""
