# Write a program which takes as input a set of integers represented by an array, and returns the size of a largest subset of integers in the array having the property that if two integers are in the subset, then so are all integers between them. For example, if the input is (3,-2,7,9,8,7,2,0, -1,5,8), the largest such subset is {-2, -1,,0,1,2,3}, so you should return 6.

from collections import defaultdict

def longest_array(arr):
    l = len(arr)
    table = {}
    for e in arr:
        if e in table:
            table[e] += 1
        else:
            table[e] = 1
    
    res = []
    visited = defaultdict(bool)

    for i in range(l):
        if not visited[arr[i]]:
            visited[arr[i]] = True
            m, n = arr[i]-1, arr[i]+1

            if not visited[m]:            
                while m in table:
                    visited[m] = True
                    m -= 1

            if not visited[n]:
                while n in table:
                    visited[n] = True
                    n += 1
            
            temp = list(range(m+1, n))
            if len(res) < len(temp):
                res = temp

    return len(res)

arr = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
print(longest_array(arr))