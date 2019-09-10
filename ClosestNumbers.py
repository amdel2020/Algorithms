from collections import defaultdict
import sys

def closestNumbers(arr):
    arr.sort()

    diffs = defaultdict(list)
    mindiff = sys.maxsize

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        diffs[diff].append(i)
        mindiff = min(mindiff, diff)
    
    result = []
    for elem in diffs[mindiff]:
        result.append(arr[elem])
        result.append(arr[elem+1])
    
    return result

arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
print(closestNumbers(arr))
