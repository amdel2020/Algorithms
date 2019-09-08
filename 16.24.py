# Pairs with Sum: Design an algorithm to find all pairs of integers within an array which sum to a specified value
# sort the array
# use binary search to find the pair => nlogn solution
# better solution => O(n) also available using dict

def find_pairs(arr, k):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n):
        left = i+1
        right = n-1
        while left < right:
            mid = (left+right) // 2
            if arr[i] + arr[mid] == k:
                result.append((arr[i], arr[mid]))
                break
            elif arr[i] + arr[left] == k:
                result.append((arr[i], arr[left]))
                break
            elif arr[i] + arr[right] == k:
                result.append((arr[i], arr[right]))
                break
            elif arr[i] + arr[mid] < k:
                left = mid+1
            else:
                right = mid-1
    
    return result

arr = [1,2,3,4,5,6,7,8,9]
k = 13
res = find_pairs(arr, k)
print(res)