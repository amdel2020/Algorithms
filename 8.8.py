def permute(arr):
    count_map = {}
    for ch in arr:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1

    keys = sorted(count_map)
    string = []
    count = []
    for key in keys:
        string.append(key)
        count.append(count_map[key])
    result = [0 for x in range(len(arr))]
    permute_util(string, count, result, 0)


def permute_util(string, count, result, level):
    if level == len(result):
        print(result)
        return

    for i in range(len(string)):
        if count[i] == 0:
            continue
        result[level] = string[i]
        count[i] -= 1
        permute_util(string, count, result, level + 1)
        count[i] += 1


if __name__ == '__main__':
    arr = ['B', 'C', 'A', 'A']
    permute(arr)
