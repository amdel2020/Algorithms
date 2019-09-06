def staircase(n):
    result = []
    for i in range(1, n+1):
        temp1 = [' ' for _ in range(n-i)]
        temp2 = ['#' for _ in range(i)]
        temp1.extend(temp2)
        result.append(temp1)

    for e in result:
        print(''.join(e))

staircase(4)