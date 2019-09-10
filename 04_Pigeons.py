'''
4. Whenever groups of pigeons gather, they instinctively establish a pecking order. For any pair of pigeons, one pigeon always pecks the other, driving
it away from food or potential mates. The same pair of pigeons always chooses the same pecking order, even after years of separation, no matter
what other pigeons are around. Surprisingly, the overall pecking order can contain cycles—for example, pigeon i pecks pigeon j, which pecks pigeon k,
which pecks pigeon `, which pecks pigeon i.

(a) Prove that any finite population of pigeons can be placed in a procession (perhaps a parade?) so that each pigeon pecks the preceding pigeon’s
posterior. Pretty please.

(b) Suppose you are given a directed graph representing the pecking relationships among a set of n pigeons. The graph contains one vertex
per pigeon, and it contains an edge i -> j if and only if pigeon i pecks pigeon j. Describe and analyze an algorithm to compute a pecking order
for the pigeons, as guaranteed by part (a).

(c) Prove that for any set of at least three pigeons, either the pecking order described in part (a) is unique, or there are three pigeons i, j, and k,
such that pigeon i pecks pigeon j, which pecks pigeon k, which pecks pigeon i.

'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.visited = [0 for i in range(self.V + 1)]
        self.parent = [-1 for i in range(self.V + 1)]
    
    def addEgde(self, u, v):
        self.graph[u].append(v)
    
    def dfsUtil(self, src):
        self.visited[src] = 1

        for v in self.graph[src]:
            if self.visited[v] == 0:
                self.parent[v] = src
                self.dfsUtil(v)

    def dfs(self):
        for v in range(1, self.V+1):
            if self.visited[v] == 0:
                self.dfsUtil(v)


g = Graph(6)
g.addEgde(1,2)
g.addEgde(2,3)
g.addEgde(3,4)
g.addEgde(4,5)
g.addEgde(5,6)
g.addEgde(6,1)

g.dfs()
print(g.parent)