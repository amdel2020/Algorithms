def balancedSums(arr):
    if len(arr) == 1:
        return 'YES'

    temp = []
    currsum = 0
    for i in range(len(arr)):        
        temp.append((currsum, -1))
        currsum += arr[i]

    currsum = 0
    for i in range(len(arr)-1, -1, -1):
        if temp[i][0] == currsum:
            return 'YES'

        temp[i] = (temp[i][0], currsum)
        currsum += arr[i]
    
    return 'NO'

arr = [0,0,2,0]
print(balancedSums(arr))