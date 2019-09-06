# Check subtree


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(src):
    result = []
    if src.left:
        result.extend(preorder_traversal(src.left))

    if src.right:
        result.extend(preorder_traversal(src.right))

    result.append(src)

    return result


def check_subtree(t1, t2):
    l1 = preorder_traversal(t1)
    l2 = preorder_traversal(t2)

    return all(elem in l2 for elem in l2)


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

res = check_subtree(node8, node6)
print(res)