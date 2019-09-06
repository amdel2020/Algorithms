def diagonalDifference(arr):
    length = len(arr)
    firstDiagonalSum = 0
    secondDiagonalSum = 0

    for i in range(length):
        firstDiagonalSum += arr[i][i]
        secondDiagonalSum += arr[i][length-1-i]
    
    if firstDiagonalSum > secondDiagonalSum:
        return firstDiagonalSum - secondDiagonalSum
    else:
        return secondDiagonalSum - firstDiagonalSum
    