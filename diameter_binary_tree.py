class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def height(node: Node):
    if node is None:
        return 0
    
    return 1 + max(height(node.left) + height(node.right))

def diameter(root: Node):
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight+rheight+1, max(ldiameter, rdiameter))
