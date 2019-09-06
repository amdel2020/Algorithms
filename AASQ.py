# Array and simple queries


def solve():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    q = [(1, 2, 4), (2, 3, 5), (1, 4, 7), (2, 1, 4)]
    for e in q:
        t, i, j = e
        temp1 = arr[:i - 1]
        temp2 = arr[i - 1:j]
        temp3 = arr[j:]
        if t == 1:
            temp2.extend(temp1)
            temp2.extend(temp3)
            arr = temp2
        elif t == 2:
            temp1.extend(temp3)
            temp1.extend(temp2)
            arr = temp1

    val = abs(arr[0] - arr[-1])
    print(val)
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    solve()

