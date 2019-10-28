class DisjointSet:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, u):
        self.parent[u] = u
        self.rank[u] = 0

    def findSet(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.findSet(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        pu = self.findSet[u]
        pv = self.findSet[v]

        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] = self.rank[pv] + 1


for i in graph:
    makeSet(i)

for u in graph:
    for v in graph[u]:
        if findSet(u) != findSet(v):
            union(u, v)
