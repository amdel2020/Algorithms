def get_adj(graph, u, v):
    r = len(graph)
    c = len(graph[0])

    adj = []
    
    if u-1 >= 0:
        adj.append((u-1, v))
    
    if u+1 < r:
        adj.append((u+1, v))
    
    if v-1 >= 0:
        adj.append((u, v-1))
    
    if v+1 < c:
        adj.append((u, v+1))
    
    if u-1 >= 0 and v-1 >= 0:
        adj.append((u-1, v-1))
    
    if u+1 < r and v+1 < c:
        adj.append((u+1, v+1))
    
    if u+1 < r and v-1 >= 0:
        adj.append((u+1, v-1))
    
    if u-1 >= 0 and v+1 < c:
        adj.append((u-1, v+1))
    
    return adj

def dfs(graph, src, visited):
    stack = [src]
    pond_size = 1

    while stack:
        u, v = stack.pop()
        visited[u][v] = True
        adj = get_adj(graph, u, v)

        for x, y in adj:
            if not visited[x][y] and graph[x][y] == 0:
                pond_size += 1
                visited[x][y] = True
                stack.append((x, y))
    
    return pond_size

graph = []
graph.append([0, 2, 1, 0])
graph.append([0, 1, 0, 1])
graph.append([1, 1, 0, 1])
graph.append([0, 1, 0, 1])

rows = 4
columns = 4
pond_sizes = []

visited = [[False for x in range(4)] for y in range(4)]
for i in range(columns):
    for j in range(rows):
        if not visited[j][i] and graph[j][i] == 0:
            src = (j, i)
            pond_sizes.append(dfs(graph, src, visited))

print(pond_sizes)
