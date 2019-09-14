#  Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not have a parent field

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def find_lca(root: Node, n1: node, n2: node) -> Node:
    if root is None:
        return None
    
    if root.left is None or root.right is None:
        return root
    
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca is not None else right_lca