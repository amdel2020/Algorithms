def equal(arr):
    result = 0
    l = len(arr)

    while True:

        min = arr[0]
        max = arr[0]
        minIndex = 0
        maxIndex = 0

        for i in range(1, l):
            if arr[i] < min:
                min = arr[i]
                minIndex = i

            elif arr[i] > max:
                max = arr[i]
                maxIndex = i

        diff = max-min

        if diff == 0:
            break
        
        closest = -1

        if diff == 1:
            closest = 1
        elif diff == 2 or diff == 3:
            closest = 2
        else:
            closest = 5

        for i in range(l):
            if i == maxIndex:
                pass
            else:
                arr[i] = arr[i] + closest
        
        result = result + 1

    return result

stri = '2 5 5 5 5 5'

arr = list(map(int, stri.rstrip().split()))
result = equal(arr)
print(result)