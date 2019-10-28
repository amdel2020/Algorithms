from queue import PriorityQueue


class Node:
    def __init__(self, index, list_num):
        self.index = index
        self.listNum = list_num


def merge(sorted_arrays):
    pq = PriorityQueue(0)
    res = []

    for idx, item in enumerate(sorted_arrays):
        pq.put((item[0], Node(0, idx)))

    while not pq.empty():
        min_node = pq.get()
        res.append(min_node[0])
        next_index = min_node[1].index + 1

        if next_index < len(sorted_arrays[min_node[1].listNum]):
            n = Node(next_index, min_node[1].listNum)
            new_item = sorted_arrays[min_node[1].listNum][next_index]
            pq.put((new_item, n))

    return res

maxRange = 1000001
arr1 = []
for i in range(2, maxRange):
	if i % 10 == 0:
		arr1.append(i)

arr2 = []
for i in range(2, maxRange):
	if i % 15 == 0:
		arr2.append(i)

arr3 = []
for i in range(2, maxRange):
	if i % 21 == 0:
		arr3.append(i)

arr = []
arr.append(arr1)
arr.append(arr2)
arr.append(arr3)

sortedarray = merge(arr)
#print(sortedarray)
