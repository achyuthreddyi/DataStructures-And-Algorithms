# Binary Tree Implementation in Python

This project implements a Binary Tree data structure in Python, providing various tree traversal methods and utility functions.

## Features

- Binary Tree construction from a list of nodes
- Tree traversal methods:
  - Pre-order traversal
  - In-order traversal
  - Post-order traversal
  - Level-order traversal
- Utility functions:
  - Count of nodes
  - Sum of node values
  - Tree height
  - Tree diameter

## Usage

To use this Binary Tree implementation:

1. Import the `BinaryTree` class from `BinaryTree.py`.
2. Create a list of node values, using -1 to represent null nodes.
3. Instantiate a `BinaryTree` object and build the tree using the `buildTree` method.
4. Use the various methods to traverse or analyze the tree.


## Implementation Details

- The `Node` class represents individual tree nodes.
- The `BinaryTree` class contains methods for tree operations.
- Tree traversal methods are implemented recursively.
- The `buildTree` method constructs the tree from a list of node values.

## TODO

- Implement iterative approaches for tree traversal methods.
- Add the following BST-specific operations:
  - Insert a node
  - Delete a node
  - Search for a value
  - Find minimum value
  - Find maximum value
  - Find successor
  - Find predecessor
  - Check if the tree is a valid BST
  - Balance the BST (e.g., convert to AVL or Red-Black tree)
  - Find the Lowest Common Ancestor (LCA) of two nodes
  - Serialize and deserialize the BST
  - Find the kth smallest element
  - Find the kth largest element
  - Print all paths from root to leaves
  - Count leaves
  - Mirror the tree
  - Check if two trees are identical
  - Find the depth of a given node
  - Print nodes at a given level
  - Print boundary nodes
  - Vertical order traversal
  - Diagonal traversal
  - Zig-zag (spiral) traversal
  - Convert BST to sorted doubly linked list
  - Construct BST from given preorder traversal
  - Find the closest element to a given value
