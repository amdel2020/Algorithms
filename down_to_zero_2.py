m = 5
arr = [-1] * m
arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 3

for i in range(m):
    if arr[i] == -1 or arr[i]  > arr[i-1] + 1:
        arr[i] = arr[i-1] + 1
    j = 1
    while j <= i and j*i < m:
        if arr[j*i] == -1 or arr[i] + 1 < arr[j*i]:
            arr[j*i] = arr[i] + 1
        j += 1

q = int(input().strip())
for i in range(q):
    n = int(input().strip())
    print(arr[n])
