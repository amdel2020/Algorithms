def missingNumbers(arr, brr):
    if len(arr) == 0:
        return sorted(list(set(brr)))

    arr.sort()
    brr.sort()

    mn = []

    j = 0
    for i in range(len(brr)):
        if arr[j] == brr[i]:
            j += 1
        else:
            mn.append(brr[i])
    
    return sorted(list(set(mn)))

def missingNumbersLinear(arr, brr):
    mn = [0 for x in range(10001)]
    result = []

    for e in arr:
        mn[e] -= 1
    
    for e in brr:
        mn[e] += 1
    
    for i in range(len(mn)):
        if mn[i] > 0:
            result.append(i)

    return result


arr = [7,2,5,3,5,3]
brr = [7,2,5,4,6,3,5,3]
mn = missingNumbersLinear(arr, brr)
print(' '.join(map(str, mn)))