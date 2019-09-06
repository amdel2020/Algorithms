from collections import defaultdict

n = int(input())
trie = defaultdict(int)

for _ in range(n):
    cmd, data = input().strip().split(' ')

    if cmd == 'add':
        for i in range(1, len(data) + 1):
            key = data[0:i]
            trie[key] += 1

    elif cmd == 'find':
        print(trie[data])