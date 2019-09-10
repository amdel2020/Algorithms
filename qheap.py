import heapq

li = []
s = set()
q = int(input().strip())
for i in range(q):
    op = input().split()
    if op[0] == '1':
        heapq.heappush(li, int(op[1]))
        s.add(int(op[1]))
    elif op[0] == '2':
        s.discard(int(op[1]))
    elif op[0] == '3':
        while li[0] not in s:
            heapq.heappop(li)
        print(li[0])