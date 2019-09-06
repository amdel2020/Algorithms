def migratoryBirds(arr):
    maxval = max(arr)
    types = [0 for x in range(maxval+1)]
    for item in arr:
        types[item] += 1
    
    result = 0
    curr = -1
    for i in range(maxval+1):
        if types[i] > curr:
            curr = types[i]
            result = i
    
    return result

arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))