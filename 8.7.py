def solve(string):
    arr = list(string)
    p = [arr[0:2], arr[1::-1]]

    for i in range(2, len(arr)):
        temp1 = [[]]
        for s in p:
            for j in range(len(s)):
                temp2 = s[:]
                temp2.insert(j, arr[i])
                temp1.append(temp2)

        temp1.pop(0)
        p = temp1
        print(p)


if __name__ == '__main__':
    solve('abcdef')
