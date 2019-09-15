# Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence. For example, if the input is <3,5,7>, (0,5), and <0,6,28>, then the output is (0, 0, 3, 5, 6, 6,7, 28).

from heapq import heappush, heappop

def merge(arr):
    min_heap = []
    arr_iters = [iter(x) for x in arr]

    for i, it in enumerate(arr_iters):
        elem = next(it, None)
        if elem is not None:
            heappush(min_heap, (elem, i))
    
    res = []
    while min_heap:
        smallest_entry, smallest_idx = heappop(min_heap)
        smallest_iter = arr_iters[smallest_idx]
        res.append(smallest_entry)
        next_elem = next(smallest_iter, None)
        if next_elem is not None:
            heappush(min_heap, (next_elem, smallest_idx))
    
    return res

arr = [[3,5,7], [0,6], [0,6,28]]
res = merge(arr)
print(res)