# 4.11

# Python3 program to print all paths
# with sum k

# utility function to print contents of
# a vector from index i to it's end


def print_vector(v, i):
    for j in range(i, len(v)):
        print(v[j])
    print()


# Binary Tree Node
""" utility that allocates a newNode  
with the given key """


class NewNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# This function prints all paths
# that have sum k
def print_path_util(root, path, k):
    # empty node
    if not root:
        return

    # add current node to the path
    path.append(root.data)

    # check if there's any k sum path
    # in the left sub-tree.
    print_path_util(root.left, path, k)

    # check if there's any k sum path
    # in the right sub-tree.
    print_path_util(root.right, path, k)

    # check if there's any k sum path that
    # terminates at this node
    # Traverse the entire path as
    # there can be negative elements too
    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]

        # If path sum is k, print path
        if f == k:
            print_vector(path, j)

    # Remove the current element
    # from the path
    path.pop(-1)


# A wrapper over printKPathUtil()
def print_path(root, k):
    path = []
    print_path_util(root, path, k)


# Driver Code
root = NewNode(1)
root.left = NewNode(3)
root.left.left = NewNode(2)
root.left.right = NewNode(1)
root.left.right.left = NewNode(1)
root.right = NewNode(-1)
root.right.left = NewNode(4)
root.right.left.left = NewNode(1)
root.right.left.right = NewNode(2)
root.right.right = NewNode(5)
root.right.right.right = NewNode(2)

k = 5
print_path(root, k)


# 10->5->3->3->-2->1->2->-3->11
# number of contiguous subsequence whose sum is K
