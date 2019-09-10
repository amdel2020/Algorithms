class DSU:
    def __init__(self, n):
        self.parent = [0] * n
        self.set_sizes = [1] * n

        for i in range(n):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root == j_root:
            return

        if self.set_sizes[i_root] >= self.set_sizes[j_root]:
            self.parent[j_root] = self.parent[i_root]
            self.set_sizes[i_root] += self.set_sizes[i_root]
        else:
            self.parent[i_root] = self.parent[j_root]
            self.set_sizes[j_root] += self.set_sizes[i_root]


n = int(input())
q = int(input())
dsu = DSU(n+1)
for _ in range(q):
    u, v = map(int, input().split())
    if u == v:
        continue
    else:
        if abs(u-v) == 1:
            dsu.union(u, v)
        else:
            if u > v:
                u, v = v, u

            while u < v:
                dsu.union(u, v)
                u += 1
                v -= 1

m = 1000000007
arr = [0] * (n+1)
res = 1
for i in range(1, n+1):
    arr[dsu.find(i)] += 1
for i in range(1, n+1):
    if arr[i] != 0:
        res = ((res % m) * 10) % m
print(res)
