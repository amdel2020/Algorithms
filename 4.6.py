# Successor
# Below algo is not correct

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_successor(node):
    if node.right is None:
        return None
    
    p = node.right

    while p.left is not None:
        p = p.left
    
    return p


node8 = BinaryTreeNode(8)
node3 = BinaryTreeNode(3)
node10 = BinaryTreeNode(10)
node1 = BinaryTreeNode(1)
node6 = BinaryTreeNode(6)
node14 = BinaryTreeNode(14)
node4 = BinaryTreeNode(4)
node7 = BinaryTreeNode(7)
node13 = BinaryTreeNode(13)

node8.left = node3
node8.right = node10

node3.left = node1
node3.right = node6

node10.right = node14

node6.left = node4
node6.right = node7

node14.left = node13

successor = inorder_successor(node10)
print(successor.data)