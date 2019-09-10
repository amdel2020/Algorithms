from collections import defaultdict, deque

# n = int(input())
# grid = [] * n

n = 8
grid = [['.', 'X', '.'], ['.', 'X', '.'], ['.', '.', '.']]

# for i in range(n):
#     grid.append(input().strip().split())

# sx, sy, gx, gy = map(int, input().strip().split())
sx, sy, gx, gy = 0, 0, 0, 2


def get_adj(g, s):
    adj = []
    n = len(g)

    x, y = s
    x -= 1
    while x >= 0:
        if g[x][y] == 'X':
            break
        adj.append((x, y))
        x -= 1

    x, y = s
    x += 1
    while x < n:
        if g[x][y] == 'X':
            break
        adj.append((x, y))
        x += 1

    x, y = s
    y -= 1
    while y >= 0:
        if g[x][y] == 'X':
            break
        adj.append((x, y))
        y -= 1

    x, y = s
    y += 1
    while y < n:
        if g[x][y] == 'X':
            break
        adj.append((x, y))
        y += 1

    return adj


def bfs(grid, sx, sy, gx, gy):
    q = deque([(sx, sy)])
    visited = defaultdict(int)
    visited[(sx, sy)] = 1

    while q:
        u = q.popleft()
        adj = get_adj(grid, u)
        for v in adj:
            if v == (gx, gy):
                return visited[u]
            if visited[v] == 0:
                visited[v] = 1 + visited[u]
                q.append(v)

    return 0

print(bfs(grid, sx, sy, gx, gy))
