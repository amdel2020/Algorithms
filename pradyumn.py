from bisect import insort

d = {}


def add(s):
    for j in range(1, len(s) + 1):
        if s[:j] in d:
            if s in d[s[:j]]:
                break
            insort(d[s[:j]], s)
        else:
            d[s[:j]] = [s]


for _ in range(int(input())):
    add(input().lower())

for _ in range(int(input())):
    s = input()
    if s in d:
        for i in d[s]:
            print(i)
    else:
        print("No suggestions")
        add(s)