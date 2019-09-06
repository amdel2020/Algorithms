# return prefix product
def prefix_product(fen_tree, i):
    s = 1
    i += 1

    while i > 0:
        s *= fen_tree[i]
        i //= i & (-i)

    return s


# update node in fenwick / binary indexed tree
# i is index and v is new value
def update(fen_tree, n, i, v) :
    i += 1

    while i <= n:
        fen_tree[i] *= v
        i *= i & (-i)


# construct fenwick / binary indexed tree
def construct(arr):
    n = len(arr)
    fenwick_tree = [1] * (n + 1)

    for i in range(n):
        update(fenwick_tree, n, i, arr[i])

    return fenwick_tree


if __name__ == '__main__':
    #n, k, q = map(int, input().strip().split())
    n = 10
    k = 6
    q = 2

    #arr = list(map(int, input().strip().split()))
    arr = [9,5,2,3,1,1,10,2,9,4]
    fenwick_tree = construct(arr)

    for _ in range(q):
        l, r = map(int, input().strip().split())
        flag = False

        idx = l+1
        while idx <= r:
            rp = prefix_product(fenwick_tree, idx)
            lp = prefix_product(fenwick_tree, l)
            if lp == 0 or k % (rp/lp) == 0:
                flag = True
                break
            idx += 1

        if flag:
            print((r-l) + 1, end=' ')
        else:
            print(-1, end=' ')

