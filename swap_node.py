from collections import deque

import sys

sys.setrecursionlimit(15000)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 0


def swap_nodes(root, h):
    q = deque([root])

    while len(q) > 0:
        node = q.popleft()

        if node.height % h == 0:
            node.left, node.right = node.right, node.left

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.key, end=' ')
        print_inorder(root.right)


n = int(input())
root = Node(1)
root.height = 1
queue = deque([root])

for _ in range(n):
    a, b = map(int, input().split())
    node = queue.popleft()
    if a != -1:
        t1 = Node(a)
        t1.height = node.height + 1
        node.left = t1
        queue.append(t1)

    if node and b != -1:
        t2 = Node(b)
        t2.height = node.height + 1
        node.right = t2
        queue.append(t2)

t = int(input())

for _ in range(t):
    k = int(input())
    swap_nodes(root, k)
    print_inorder(root)
    print()
