from collections import defaultdict

n = int(input())
strings = defaultdict(int)

for _ in range(n):
    s = input().strip()
    strings[s] += 1

q = int(input())

for _ in range(q):
    s = input().strip()
    print(strings[s])