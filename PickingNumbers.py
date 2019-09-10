def pickingNumbers(a):
    a.sort() 
    # [1,1,2,2,2,3]
    currlen = 1
    maxlen = 0
    i = 0
    diff = 0

    while True:
        if i == len(a)-1:
            maxlen = max(maxlen, currlen)
            break

        if a[i+1] - a[i] == 0:
            currlen += 1
        elif a[i+1] - a[i] == 1:
            if diff < 1:
                currlen += 1
                diff += 1
            else:
                diff = 0                
                maxlen = max(maxlen, currlen)
                currlen = 1
        else:
            diff = 0
            maxlen = max(maxlen, currlen)
            currlen = 1
        
        i += 1
    
    return maxlen

a = [1,2,2,3,1,2]
print(pickingNumbers(a))