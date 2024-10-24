# Singly Linked List

A singly linked list is a linear data structure in which elements are stored in nodes. Each node contains a data field and a reference (link) to the next node in the sequence.

## Operations

The following operations are typically performed on a singly linked list:

1. **Insertion**
   - Insert at the beginning
   - Insert at the end
   - Insert at a specific position

2. **Deletion**
   - Delete from the beginning
   - Delete from the end
   - Delete from a specific position
   - Delete a node with a specific value

3. **Traversal**
   - Print all elements
   - Count the number of nodes

4. **Search**
   - Find if an element exists
   - Get the position of an element

5. **Update**
   - Update the value of a node at a specific position

6. **Other Operations**
   - Reverse the list
   - Detect a cycle in the list
   - Find the middle element
   - Merge two sorted linked lists
   - Remove duplicates from a sorted list
   - Check if the list is a palindrome

## Time Complexity

- Access: O(n)
- Search: O(n)
- Insertion: O(1) at the beginning, O(n) at the end or middle
- Deletion: O(1) at the beginning, O(n) at the end or middle

## Space Complexity

- O(n) for n elements

## Advantages

- Dynamic size
- Efficient insertion and deletion at the beginning

## Disadvantages

- Sequential access only
- Extra memory for storing references

## Implementation

The implementation of these operations can be found in the `sl_list.py` file in this directory.

