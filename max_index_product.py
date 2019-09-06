from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, -1)

stack = [(1, arr[1])]
right = defaultdict(int)

for i in range(2, n+1):
    if len(stack) > 0:
        elem = stack.pop()
        while elem[1] < arr[i]:
            right[elem[0]] = i
            if len(stack) == 0:
                break
            elem = stack.pop()

        if elem[1] >= arr[i]:
            stack.append(elem)

    stack.append((i, arr[i]))

while len(stack) > 0:
    elem = stack.pop()
    right[elem[0]] = 0

stack.clear()
stack = [(n, arr[n])]
left = defaultdict(int)

for i in range(n-1, 0, -1):
    if len(stack) > 0:
        elem = stack.pop()
        while elem[1] < arr[i]:
            left[elem[0]] = i
            if len(stack) == 0:
                break
            elem = stack.pop()

        if elem[1] >= arr[i]:
            stack.append(elem)

    stack.append((i, arr[i]))

while len(stack) > 0:
    elem = stack.pop()
    left[elem[0]] = 0

mip = 0

for e in left:
    mip = max((left[e]) * (right[e]), mip)

print(mip)
