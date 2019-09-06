# working segment tree


def build(node, start, end, tree, arr):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid, tree, arr)
        build(2 * node + 1, mid + 1, end, tree, arr)

        tree[node] = min(tree[2 * node], tree[2 * node + 1])


def update(node, start, end, idx, val, tree, arr):
    if start == end:
        arr[idx] = val
        tree[node] = val
    else:
        mid = (start + end) // 2

        if start <= idx <= mid:
            update(2 * node, start, mid, idx, val, tree, arr)
        else:
            update(2 * node + 1, mid + 1, end, idx, val, tree, arr)

        tree[node] = min(tree[2 * node], tree[2 * node + 1])


def query(node, start, end, l, r, tree):
    if l > end or start > r:
        return float('inf')

    if l <= start and r >= end:
        return tree[node]

    mid = (start + end) // 2

    p1 = query(2 * node, start, mid, l, r, tree)
    p2 = query(2 * node + 1, mid + 1, end, l, r, tree)

    return min(p1, p2)


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    tree = [0] * (4 * n + 2)

    build(1, 1, n, tree, arr)

    for _ in range(q):
        q, x, y = input().split()
        x = int(x)
        y = int(y)

        if q == 'q':
            m = query(1, 1, n, x, y, tree)
            print(m)
        elif q == 'u':
            update(1, 1, n, x, y, tree, arr)
