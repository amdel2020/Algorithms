# 4.7 Build order

from collections import defaultdict

time = 0
finish_time = []
color = {}


def dfs(g):
    global color
    for u in g:
        color[u] = 0

    for u in g:
        if color[u] == 0:
            dfs_visit(g, u)


def dfs_visit(g, u):
    global time
    global finish_time
    global color

    time += 1
    color[u] = 1
    for v in g[u]:
        if color[v] == 0:
            dfs_visit(g, v)

    color[u] = 2
    time += 1
    finish_time.insert(0, u)


graph = defaultdict(list)
graph['e']
graph['a'].append('d')
graph['c']
graph['f'].append('a')
graph['f'].append('b')
graph['b'].append('d')
graph['d'].append('c')

dfs(graph)
print(finish_time)
