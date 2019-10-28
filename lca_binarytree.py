class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def least_common_ancestor(root, n1, n2):
    if root is None:
        return None

	if root.data == n1 or root.data == n2:
		return root

    left = least_common_ancestor(root.left, n1, n2)
    right = least_common_ancestor(root.right, n1, n2)

    if right and left:
     	return root

    return left if left is not None else right