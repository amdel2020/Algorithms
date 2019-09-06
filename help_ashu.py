def update(bit, idx, val):
    n = len(bit)
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

def query(bit, idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx

    return s

if __name__ == '__main__':
    n = int(input().strip())
    arr = [i%2 for i in list(map(int, input().strip().split()))]
    bit = [0] * (n + 1)

    for i in range(n):
        update(bit, i+1, arr[i])

    q = int(input())
    for i in range(q):
        q, x, y = map(int, input().split())
        if q == 0:
            update(bit, x, y)
        elif q == 1:
            print(query(bit, y) - query(bit, x-1) + 1)
        elif q == 2:
            print(query(bit, y) - query(bit, x-1) + 1)

