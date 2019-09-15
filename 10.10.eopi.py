# Design an algorithm that computes the successor of a node in a binary tree. Assume that each node stores its parent.

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

def find_successor(node: Node) -> Node:
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    
    while node.parent and node.parent.right is node:
        node = node.parent
    
    return node.parent
    
