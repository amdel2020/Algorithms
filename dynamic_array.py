n, q = map(int, input().split())

seqList = [[] for _ in range(n)]
last_answer = 0

for _ in range(q):
    q, x, y = map(int, input().split())
    idx = (x ^ last_answer) % n

    if q == 1:
        seq = seqList[idx]
        seq.append(y)

    elif q == 2:
        seq = seqList[idx]
        last_answer = seq[y % len(seq)]
        print(last_answer)
