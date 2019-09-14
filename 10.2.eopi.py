# Write a program that checks whether a binary tree is symmetric

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def check_symmetry(left: Node, right: Node) -> bool:
    if left is None and right is None:
        return True
    
    if left is not None and right is not None:
        return left.data == right.data \
                and check_symmetry(left.left, right.right) \
                and check_symmetry(left.right, right.left)
    
    return False

def is_symmetric(root: Node) -> bool:
    return root == None or check_symmetry(root.right, root.left)

root = Node(6)
root.left = Node(4)
root.right = Node(7)
print(is_symmetric(root))
