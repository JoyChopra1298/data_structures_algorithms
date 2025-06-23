# Tree

A tree is a hierarchical and non-linear data structure that consists of nodes connected with edges. 
Each node has only one parent (except root node). A tree is a graph with no cycles (acyclic)

## Key terms

1. **Root node** - The topmost node in the tree.
2. **Parent node** - A node with child nodes
3. **Child node** - A node that descends from another node
4. **Lead node** - A node with no children
5. **Subtree** - A tree formed by a particular node and its descendants
6. **Depth of a node** - Number of edges from root to that node
7. **Height of the tree** - Number of edges in the longest path from root to a leaf 

## Usecases

1. To represent hierarchical data like file system, family trees
2. Useful for searching and sorting large datasets (BST)
3. Useful for database indexing (B-tree)
4. Useful for autocomplete (Trie)

## N-ary tree

In a n-ary tree, each node can have at most n children. It is useful for file systems, HTML/XML parsing, AI trees, and organisational charts.

## Operations

| Number | Operation | Description | Time Complexity |
| -- | -- | -- | -- |
| 1 | Create() | Create a new empty tree | O(1) |
| 2 | Insert(value) | Insert value in the tree | O(n) |
| 3 | Remove(value) | Remove node with a particular value | O(n) |
| 4 | Search(value) | Find node with a particular value | O(n) |
| 5 | Traverse() | Visit all nodes of the tree - BFS/DFS | O(n) |

Here, n = Number of nodes in the tree
