def dfs(graph, r, c):
    visited = [[0 for x in range(c)] for y in range(r)]
    parent = [[(-1, -1) for x in range(c)] for y in range(r)]
    visited[0][0] = 1
    stack = [(0, 0)]

    while stack:
        u, v = stack.pop()
        edges = []
        if v == r-1 and u == c-1:
            break
        elif v >= r-1:
            edges.append((u+1, v))
        elif u >= c-1:
            edges.append((u, v+1))
        else:
            edges.append((u, v + 1))
            edges.append((u+1, v))

        for x, y in edges:
            if visited[x][y] == 0 and graph[x][y] != 1:
                visited[x][y] = 1
                parent[x][y] = (u, v)
                stack.append((x, y))

    dx = 3
    dy = 3
    path = [(dx, dy)]

    while True:
        dx, dy = parent[dx][dy]
        path.insert(0, (dx, dy))
        if dx == 0 and dy == 0:
            break

    return path


def solve():
    r = 4
    c = 4
    graph = [[0 for x in range(c)] for y in range(r)]
    graph[1][2] = 1
    graph[0][3] = 1
    dfs(graph, r, c)


if __name__ == '__main__':
    solve()
