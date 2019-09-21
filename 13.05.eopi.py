
def nearest_repeated_entries(arr):
    res = float('inf')
    d = dict()

    for i in range(len(arr)):
        if arr[i] in d:
            res = min(res, i - d[arr[i]])
        
        d[arr[i]] = i
    
    return res

arr = ['all', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
print(nearest_repeated_entries(arr))
