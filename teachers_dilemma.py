class DisjointSet:
    def __init__(self, count):
        self.parent = [0] * count
        self.size_of_sets = [1] * count # used for rank

        for i in range(count):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i]) # used for path compression
        return self.parent[i]

    def union(self, i, j):
        i_rep = self.find(i)
        j_rep = self.find(j)

        if i_rep == j_rep: # belongs to same set
            return

        self.parent[i_rep] = j_rep # make jrep as parent of irep
        self.size_of_sets[j_rep] += self.size_of_sets[i_rep]
        self.size_of_sets[i_rep] = 0


n, m = map(int, input().split())
disjoint_set = DisjointSet(n)

for _ in range(m):
    u, v = map(int, input().split())
    disjoint_set.union(u-1, v-1)

no_of_ways = 1
for num in disjoint_set.size_of_sets:
    if num > 0:
        no_of_ways *= num

print(no_of_ways % 1000000007)
