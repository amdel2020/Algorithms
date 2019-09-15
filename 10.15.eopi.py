# Write a program that computes the exterior of a binary tree.

class Node:
    def __init__(self, data: int):
        self.data:int = data
        self.left: Node = None
        self.right: Node = None

def exterior(root: Node):
    
    def get_leaves(root: Node):
        if not root:
            return None
        
        if not root.left and not root.right:
            return [root]

        return get_leaves(root.left) + get_leaves(root.right)
    
    def left_exterior(root: Node):
        ext = []
        itr = root

        while itr:
            ext.append(itr)
            itr = itr.left
        
        ext.pop()
        return ext
    
    def right_exterior(root: Node):
        ext = []
        itr = root

        while itr:
            ext.append(itr)
            itr = itr.right
        
        ext.pop()
        ext.pop(0)
        return ext
    
    return left_exterior(root) + get_leaves(root) + right_exterior(root)