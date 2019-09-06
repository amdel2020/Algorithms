def maxSubArrays(arr):
    return [maxSubArrayLinear(arr), maxSubSeq(arr)]

def maxSubArray(arr):

    l = len(arr)
    result = [[0 for x in range(l)] for y in range(l)]
    
    for i in range(len(arr)):
        result[i][i] = arr[i]

    for i in range(2, l+1):
        row = 0
        for j in range(0, l-i+1):
            k = j+i-1
            num = sum(arr[j:k+1])
            a = result[row][k-1]
            b = result[row+1][k]
            result[row][k] = max([num, a, b])
            row += 1

    return result[0][l-1]

def maxSubSeq(arr):
    result = max(arr)

    if result < 0:
        return result
    else:
        result = 0

    for elem in arr:
        if elem > 0:
            result += elem
    
    return result

def maxSubArrayLinear(arr):
    if max(arr) < 0:
        return max(arr)

    maxi = 0
    currMax = 0

    for e in arr:
        currMax += e

        if currMax < 0:
            currMax = 0
        
        if currMax > maxi:
            maxi = currMax
    
    return maxi


arr = [-2, -3, -1, -4, -6]
maxSubArrays(arr)