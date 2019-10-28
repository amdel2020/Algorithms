# Kruskal algorithm for finding minimum spanning tree

class Graph:
    def __init__(self):
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph.append([v, u, w])

    def mstKruskal(self):
        tree = set()

        for item in self.graph:
            makeSet(item[0])

        self.graph.sort(key = lambda k: k[2])

        for item in self.graph:
            if findSet(item[0]) != findSet(item[1]):
                tree = tree.union([item[0], item[1]])
                union(item[0], item[1])

        return tree
