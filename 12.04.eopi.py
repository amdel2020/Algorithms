def square_root(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq <= n:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

print(square_root(8))