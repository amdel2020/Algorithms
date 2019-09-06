def birthdayCakeCandles(ar):
    count = 1
    ar.sort(reverse=True)
    curr = ar[0]

    index = 1
    while True:
        if index < len(ar) and ar[index] == curr:
            count += 1
            index += 1
        else:
            break
    
    return count

ar = [3,2,1,3]
print(birthdayCakeCandles(ar))