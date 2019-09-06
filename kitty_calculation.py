from collections import defaultdict, deque

tr = defaultdict(list)
dist = defaultdict(int)
queries = []
with open('kitty_calculation.txt') as fp:
    n, q = map(int, fp.readline().split())
    for i in range(1, n):
        a, b = map(int, fp.readline().split())
        tr[a].append(b)
        tr[b].append(a)
    for i in range(q):
        k = int(fp.readline().strip())
        s = set(map(int, fp.readline().strip().split()))
        queries.append(s)


def bfs(tr, src, dist):
    v = [False] * (len(tr)+1)
    di = [0] * (len(tr)+1)
    q = deque([src])

    while len(q) > 0:
        x = q.popleft()
        v[x] = True
        for y in tr[x]:
            if v[y] is False:
                q.append(y)
                di[y] = di[x] + 1
                dist[(src, y)] = di[y]


for src in tr:
    bfs(tr, src, dist)


def get_all_pairs(q):
    res = []

    if len(q) == 1:
        return []

    if len(q) == 2:
        temp = list(q)
        return [(temp[0], temp[1])]

    for i in range(len(q)-1):
        for j in range(i+1, len(q)):
            temp = list(q)
            res.append((temp[i], temp[j]))

    return res


for q in queries:
    sum_exp = 0
    pairs = get_all_pairs(q)
    for s in pairs:
        temp = s[0] * s[1]
        temp *= dist[(s[0], s[1])]
        sum_exp += temp
    print(sum_exp)

