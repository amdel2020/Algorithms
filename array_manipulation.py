n, m = map(int, input().strip().split())
arr = [0] * (n+1)

for _ in range(m):
    l, r, v = map(int, input().split())
    arr[l-1] += v
    if (r <= len(arr)): arr[r] -= v;

max = curr = 0
for i in arr:
   curr= curr + i
   if max<curr:
       max=curr
print(max)