# Write a nonrecursive program for computing the inorder traversal sequence for a binary tree.

# Python program to do inorder traversal without recursion and  
# without stack Morris inOrder Traversal 

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def morris_traversal(root):
    iterator: Node = root

    while iterator is not None:
        if iterator.left is None:
            print(iterator.data)
            iterator = iterator.right
        
        else:
            pre: Node = iterator.left
            while pre.right is not None and pre.right != iterator:
                pre = pre.right
            
            if pre.right is None:
                pre.right = iterator
                iterator = iterator.left
            else:
                pre.right = None
                print(iterator.data)
                iterator = iterator.right