def getTotalX(a, b):
    maxa = max(a)
    minb = min(b)

    result = 0
    for i in range(maxa, minb+1):  
        flag = True      
        for elem in a:
            if i % elem != 0:
                flag = False
                break
        
        if flag == True:
            for elem in b:
                if elem % i != 0:
                    flag = False
                    break
        
        if flag == True:
            result += 1
    
    return result

a = [2,4]
b = [16,32,96]
print(getTotalX(a,b))