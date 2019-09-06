q = int(input())
stack = []
S = ''
for i in range(q):
    op = input().split()
    if op[0] == '1':
        stack.append(S)
        S = S + op[1]
    elif op[0] == '2':
        stack.append(S)
        k = int(op[1])
        S = S[:-k]
    elif op[0] == '3':
        k = int(op[1])
        print(S[k-1])
    elif op[0] == '4':
        if stack:
            S = stack.pop()
