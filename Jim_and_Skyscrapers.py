# n = int(input())
# arr = list(map(int, input().split()))
from collections import defaultdict

n = 6
arr = [3, 2, 1, 2, 3, 3]
count = 0
cache = defaultdict(int)

s1 = [arr[0]]
s2 = []

for i in range(1, n):
    elem = s1[-1]
    if arr[i] >= elem:
        j = i
        while s1 and s1[-1] <= arr[i]:
            temp = s1.pop()
            j -= 1
            if temp == arr[i]:
                count += 1
                count += cache[j]
                cache[i] = 1 + cache[j]
                s1.append(temp)
                break

            s2.append(temp)
        while s2:
            s1.append(s2.pop())

    s1.append(arr[i])

print(2 * count)
