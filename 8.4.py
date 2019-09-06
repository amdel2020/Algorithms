import copy


def solve(ar):
    length = len(ar)
    p = [set([]), {ar[0]}]

    for i in range(1, length):
        temp = copy.deepcopy(p)
        for s in temp:
            s.add(ar[i])
        p.extend(temp)

    return p


if __name__ == '__main__':
    arr = [i for i in range(25)]
    power_set = solve(arr)
    print(power_set)
    print(len(power_set))
