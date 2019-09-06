def solve(n):
    a = 1
    b = 2
    c = 4
    d = 0

    for i in range(4, n + 1):
        d = a + b + c
        a = b
        b = c
        c = d

    return d


if __name__ == '__main__':
    print(solve(1000))
