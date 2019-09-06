class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min = float('inf')
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, arr):
        self.root = self.__build(arr, 0, len(arr)-1)

    def __build(self, arr, left, right):
        if left > right:
            return None

        if left == right:
            node = SegmentTreeNode(left, right)
            node.min = arr[left]
            return node

        mid = int((left + right) / 2)
        root = SegmentTreeNode(left, right)

        root.left = self.__build(arr, left, mid)
        root.right = self.__build(arr, mid+1, right)
        root.min = min(root.left.min, root.right.min)

        return root

    def __update_util(self, root, idx, val):
        if root.start == root.end:
            root.min = val
            return val

        mid = int((root.start + root.end) / 2)

        if idx <= mid:
            self.__update_util(root.left, idx, val)
        else:
            self.__update_util(root.right, idx, val)

        root.min = min(root.left.min, root.right.min)

        return root.min

    def __min_range_util(self, root, i, j):
        if root.start == i and root.end == j:
            return root.min

        mid = int((root.start + root.end) / 2)

        if j <= mid:
            return self.__min_range_util(root.left, i, j)
        elif i >= mid+1:
            return self.__min_range_util(root.right, i, j)
        else:
            return min(self.__min_range_util(root.left, i, mid), self.__min_range_util(root.right, mid+1, j))

    def update(self, idx, val):
        return self.__update_util(self.root, idx, val)

    def min_range(self, i, j):
        return self.__min_range_util(self.root, i, j)


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    segment_tree = SegmentTree(arr)

    for _ in range(q):
        q, x, y = input().split()
        i = int(x)-1
        j = int(y)-1

        if q == 'q':
            m = segment_tree.min_range(i, j)
            print(m)
        elif q == 'u':
            segment_tree.update(i, j)

