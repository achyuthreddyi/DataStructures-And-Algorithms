class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left_node = None
        self.right_node = None
        

class BST():
    def __init__(self) -> None:
        self.root = None
    
    def insert_data(self, root_node: Node, item: int):
        if not root_node:
            return Node(item)
        
        if root_node.data > item:
            root_node.left_node = self.insert_data(root_node.left_node, item)
        
        if root_node.data < item:
            root_node.right_node = self.insert_data(root_node.right_node, item)
        
        return root_node
    
    def create_bst(self, data: list[int]):
        
        for item in data:
            if not self.root:
                self.root = Node(item)
            else:
                self.insert_data(self.root, item)
        
        return self.root
            
    def inorder_traversal(self, root):
        if not root:
            return
        
        self.inorder_traversal(root.left_node)
        print(root.data)
        self.inorder_traversal(root.right_node)
        
    def search_key(self, node: Node, key):
        
        if not node:
            return False
        
        if node.data == key:
            return True
        
        if node.data > key:
            return self.search_key(node.left_node, key)
        
        return self.search_key(node.right_node, key)
    
    def delete_key(self, node: Node, key):
        if not node:
            return None
        
        if node.data > key:
            node.left_node = self.delete_key(node.left_node, key)
        elif node.data < key:
            node.right_node = self.delete_key(node.right_node, key)
        else:
            # Case 1
            if not node.left_node and not node.right_node:
                return None
            # Case 2
            if not node.left_node:
                return node.right_node
            
            if not node.right_node:
                return node.left_node 
            # Case 3
            inorder_successor: Node = self.inorder_successor(node.right_node)
            node.data = inorder_successor.data
            node.right_node = self.delete_key(node.right_node, inorder_successor.data)
        
        return node
            
    def inorder_successor(self, node: Node):
        current: Node = node
        while current.left_node:
            current = current.left_node
            
        return current
     
data: list[int] = [5, 1, 3, 4, 2, 7]
bst: BST = BST()
root_node: BST = bst.create_bst(data)
bst.inorder_traversal(root_node)

print(bst.search_key(root_node, 5))
print(bst.search_key(root_node, 9))
root_node = bst.delete_key(root_node, 3)
print('here1')
bst.inorder_traversal(root_node)