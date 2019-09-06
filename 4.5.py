# 4.5 Validate BST


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def validate_bst(root):
    if root is None or (root.left is None and root.right is None):
        return True

    if root.left and root.data < root.left.data:
        return False

    if root.right and root.data > root.right.data:
        return False

    return validate_bst(root.left) and validate_bst(root.right)


def main():
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

    print(validate_bst(node8))


if __name__ == '__main__':
    main()
