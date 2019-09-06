# 1,2,3,4,5
# i = 0, j = 1, d = 1
# i = 0, j = 2, d = 2, c++
# i = 1, j = 2, d = 1,
# i = 1, j = 3, d = 2, c++,
# i = 2, j = 3, d = 1
# i = 2, j = 4, d = 2, c++

def pairs(k, arr):
    arr.sort()
    l = len(arr)
    count = 0

    i = 0
    j = 1

    while j < l:
        diff = arr[j] - arr[i]

        if diff == k:
            count += 1
            j += 1
        elif diff > k:
            i += 1
        else:
            j += 1
    
    return count

arr = [1,2,3,4,5,6,8]
print(pairs(2, arr))