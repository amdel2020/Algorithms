from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.parent = defaultdict()
        self.dist = defaultdict()

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def initializeSingleSource(self, src):
        for u in self.graph:
            self.parent[u] = None
            self.dist[u] = float('inf')
        self.dist[src] = 0

    def relax(self, u, v, w):
        if self.dist[v] > self.dist[u] + w:
            self.dist[v] = self.dist[u] + w
            self.parent[v] = u

    def bellmanFord(self, src):
        self.initializeSingleSource(src)
        for _ in range(self.vertices):
            for item in self.graph:
                self.relax(item[0], item[1], item[2])
        for item in self.graph:
            if self.dist[item[0]] > self.dist[item[1]] + w:
                return False
        return True
