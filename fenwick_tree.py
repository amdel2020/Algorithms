class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * size

    def add(self, index, value):
        while 0 < index <= self.size:
            self.tree[index - 1] += value
            index += index & -index

    def sub(self, index, value):
        while 0 < index <= self.size:
            self.tree[index - 1] -= value
            index += index & -index

    def prefix_sum(self, index):
        sm = 0
        while 0 < index <= self.size:
            sm += self.tree[index - 1]
            index -= index & -index
        return sm


n = int(input())
array = list(map(int, input().split()))
otree = FenwickTree(n)
etree = FenwickTree(n)
for i in range(len(array)):
    if (array[i] & 1) == 1:
        otree.add(i + 1, 1)
    else:
        etree.add(i + 1, 1)
q = int(input())
while q > 0:
    q -= 1
    code, a, b = map(int, input().split())
    if code == 0:
        if (array[a - 1] & 1) == 0 and (b & 1) == 1:
            array[a - 1] = b
            otree.add(a, 1)
            etree.sub(a, 1)
        elif (array[a - 1] & 1) == 1 and (b & 1) == 0:
            array[a - 1] = b
            otree.sub(a, 1)
            etree.add(a, 1)
    elif code == 1:
        print(etree.prefix_sum(b) - etree.prefix_sum(a - 1))
    elif code == 2:
        print(otree.prefix_sum(b) - otree.prefix_sum(a - 1))
