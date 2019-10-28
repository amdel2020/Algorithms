
def findSmallest(arr, n): 
  
    res = 1 
    for i in range (0, n ): 
        if arr[i] <= res: 
            res = res + arr[i] 
        else: 
            break
    return res 

arr1 = [1, 3, 4, 5] 
n1 = len(arr1) 
print(findSmallest(arr1, n1)) 
  
arr2= [1, 2, 6, 10, 11, 15] 
n2 = len(arr2) 
print(findSmallest(arr2, n2)) 
  
arr3= [1, 1, 1, 1] 
n3 = len(arr3) 
print(findSmallest(arr3, n3)) 
  
arr4 = [1, 1, 3, 4] 
n4 = len(arr4) 
print(findSmallest(arr4, n4)) 