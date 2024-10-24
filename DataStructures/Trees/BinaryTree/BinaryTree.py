class Node():
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
        

class BinaryTree():
    index = -1
    
    def buildTree(self, nodes):
        self.index += 1
            
        if nodes[self.index] == -1:
            return None
            
        new_node = Node(nodes[self.index])
        new_node.left_node = self.buildTree(nodes)
        new_node.right_node = self.buildTree(nodes)
        
        return new_node
    
    def pre_order_traversal_print(self, root: Node):
        if not root:
            return
        print(root.data, end=' ')
        self.pre_order_traversal_print(root.left_node)
        self.pre_order_traversal_print(root.right_node)
        
    def in_order_traversal_print(self, root: Node):
        if not root:
            return
        self.in_order_traversal_print(root.left_node)
        print(root.data, end=' ')
        self.in_order_traversal_print(root.right_node)
        
    def post_order_traversal_print(self, root: Node):
        if not root:
            return
        self.post_order_traversal_print(root.left_node)
        self.post_order_traversal_print(root.right_node)
        print(root.data, end=' ')
        
    # TODO: Implement iterative approach for these
    
    def level_order_traversal(self, root: Node):
        if not root:
            print('Tree does not esist to print')
            return
        
        queue: list[Node] = []
        
        queue.append(root)
        queue.append(None)
        
        while queue:
            currNode: Node = queue.pop(0)
            
            if not currNode:
                print('\n')
                if not queue:
                    break
                else:
                    queue.append(None)
            else:
                print(currNode.data)
                if currNode.left_node:
                    queue.append(currNode.left_node)
                if currNode.right_node:
                    queue.append(currNode.right_node)
                    
    def count_of_nodes(self, root: Node):
        if not root:
            return 0
        
        left_count = self.count_of_nodes(root.left_node)
        right_count = self.count_of_nodes(root.right_node)
        
        return left_count + right_count + 1
    
    def sum_of_nodes(self, root: Node):
        if not root:
            return 0
        
        left_sum = self.sum_of_nodes(root.left_node)
        right_sum = self.sum_of_nodes(root.right_node)
        
        return left_sum + right_sum + root.data
        
    def height(self, root: Node):
        if not root:
            return 0
        
        left_height = self.height(root.left_node)
        right_height = self.height(root.right_node)
        
        return max(left_height, right_height) + 1
    
    def diameter(self, root: Node):
        if not root:
            return 0
        if not root.left_node and not root.right_node:
            return 1
        else:
            return 1 + max(self.diameter(root.left_node), self.diameter(root.right_node))
        
        
nodes: list[int] = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
print(len(nodes))
bt = BinaryTree()
root: Node = bt.buildTree(nodes)
# print(root.data)
# print('Pre order Traversal')
# bt.pre_order_traversal_print(root)
# print('\nIn order Traversal')
# bt.in_order_traversal_print(root)
# print('\nPost order Traversal')
# bt.post_order_traversal_print(root)
print('Level Order Traversal')
# bt.level_order_traversal(root)

# print(bt.count_of_nodes(root))
# print(bt.sum_of_nodes(root))
print(bt.height(root))
print('diameter', bt.diameter(root))
