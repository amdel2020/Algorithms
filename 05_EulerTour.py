'''
An Euler tour of a graph G is a closed walk through G that traverses every edge of G exactly once.

(a) Prove that if a connected graph G has an Euler tour, then every vertex in G has even degree. (Euler proved this.)

(b) Prove that if every vertex in a connected graph G has even degree, then G has an Euler tour. (Euler did not prove this.)

(c) Describe and analyze an algorithm to compute an Euler tour in a given graph, or correctly report that no such tour exists. (Euler vaguely waved
his hands at this.)
'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)``
