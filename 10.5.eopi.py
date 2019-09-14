class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def tree_path_sum(root: Node, val: int) -> int:
    if root is None:
        return 0
    
    val = val*10 + root.data

    if root.left is None and root.right is None:
        return val
    
    return tree_path_sum(root.left, val) + tree_path_sum(root.right, val)

root = Node(6) 
root.left = Node(3) 
root.right = Node(5) 
root.left.left = Node(2) 
root.left.right = Node(5) 
root.right.right = Node(4) 
root.left.right.left = Node(7) 
root.left.right.right = Node(4) 
print(tree_path_sum(root, 0))