# Write a program that takes an array and returns the length of a longest subarray with the property that all its elements are distinct. Forexample,if the array is (f,s,f,e,t,w,e,n,w,e) then a longest subarray all of whose elements are distinct is (s, f ,e,t,w).

def longest_subarray(arr):
    idx = 0
    j = 0
    table = {}
    res = []
    
    while idx < len(arr):
        if arr[idx] in table:
            temp = arr[j:idx]
            if len(temp) > len(res):
                res = temp
            j = table[arr[idx]] + 1
        
        table[arr[idx]] = idx        
        idx += 1

    if len(arr[j:]) > len(res):
        return arr[j:]

    return res

arr = ['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e', 'a', 'c', 'd', 'x', 'z']
print(longest_subarray(arr))
