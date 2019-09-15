# Given an inorder traversal sequence and a preorder traversal sequence of a binary tree write a program to reconstruct the tree. Assume each node has a unique key.

class Node:
    def __init__(self, data: int):
        self.data:int = data
        self.left: Node = None
        self.right: Node = None

def construct_tree(preorder, inorder) -> Node:
    inorder_dict = {data: i for i, data in enumerate(inorder)}

    def construct_tree_helper(preorder_start, preorder_end, inorder_start, inorder_end) -> Node:
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        root_idx = inorder_dict[preorder[preorder_start]]
        left_subtree_size = root_idx - inorder_start

        node = Node(preorder[preorder_start])
        node.left = construct_tree_helper(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_idx)
        node.right = construct_tree_helper(preorder_start + 1 + left_subtree_size, preorder_end, root_idx + 1, inorder_end)

        return node
    
    return construct_tree_helper(0, len(preorder), 0, len(inorder))


inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
preorder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
root = construct_tree(preorder, inorder)
print(root)

