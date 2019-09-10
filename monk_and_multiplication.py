from functools import reduce
from heapq import heappush, heappop

n = int(input())
arr = [-int(x) for x in input().split()]
h = []

for num in arr:
    heappush(h, num)
    if len(h) <= 2:
        print(-1)
    elif len(h) == 3:
        print(reduce((lambda x, y: x * y), h) * -1)
    else:
        a = heappop(h)
        b = heappop(h)
        c = heappop(h)
        print(-1 * a * b * c)
        heappush(h, c)
        heappush(h, b)
        heappush(h, a)

