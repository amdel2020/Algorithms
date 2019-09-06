from random import random


class Treap:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index <= self.left.size:
            return self.left[index]

        index -= self.left.size if self.left else 0

        if index == 1:
            return self.val

        return self.right[index - 1]

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.val) + ' '
        res += str(self.right) if self.right else ''
        return res


def merge(left, right):

    if not (left and right):
        return left or right

    if left.priority > right.priority:
        left.size += right.size
        left.right = merge(left.right, right)
        return left

    right.size += left.size
    right.left = merge(left, right.left)
    return right


def split(t, index):
    if not index:
        return None, t
    if not t:
        return None, None

    if index == t.size:
        return t, None

    if t.left and t.left.size >= index:
        res, t.left = split(t.left, index)
        t.size -= res.size
        return res, t

    index -= t.left.size if t.left else 0

    if index == 1:
        temp = t.right
        t.right = None
        t.size -= temp.size
        return t, temp

    t.right, leftover = split(t.right, index - 1)
    t.size -= leftover.size
    return t, leftover


def handle(t, key, start, end):
    start -= 1
    left, t = split(t, start)
    t, right = split(t, end - start)
    res = merge(left, right)

    if key == 1:
        res = merge(t, res)
    else:
        res = merge(res, t)

    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))
t = Treap(a[0], random())

for i in a[1:]:
    t = merge(t, Treap(i, random()))

for _ in range(m):
    t = handle(t, *map(int, input().split()))
print(abs(t[1] - t[n]))
print(t)