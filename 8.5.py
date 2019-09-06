def solve(x, y):
    mul = 0

    for _ in range(x):
        mul += y

    return mul


if __name__ == '__main__':
    print(solve(12, 100))
