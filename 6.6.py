# c(i,j) = min{ c(i,k) + c(k+1, j) + m(i-1)*m(k)*m(j)} => formula for chain matrix mutliplication
# bbbbac => parenthesize in such a way that result is a
# DP =>
# len(s) = n, substring of len (i, j)
# fn(x,y) => either is result is a or not a
# as recursive sub problem
# 1, k
# i,j => split at k such that (i,k) is a or b and (k+1,j) is c || (i,k) is c and (k+1,j) is a



# if a[i] == b[j]
    # max = 1 + s[i-1, j-1]
# else
    # max = max{ s[i-1,j], s[i, j-1] }


a = list('zxabcdezy')
b = list('yzabcdezx')
m = len(a)
n = len(b)

s = [[0 for x in range(m+1)] for y in range(n+1)]
maximum = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[j-1] == b[i-1]:
            s[i][j] = 1 + s[i-1][j-1]
        else:
            s[i][j] = 0
        
        maximum = max(maximum, s[i][j])

print(maximum)