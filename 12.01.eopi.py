def search_first_k(arr, k):
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > k:
            right = mid - 1
        elif arr[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

arr = [-14, -10, 2, 108, 108, 108, 243, 285, 285, 285, 401]
print(search_first_k(arr, 108))
