from bisect import bisect_left


class MedianFinder:
    def __init__(self):
        self.items = []

    def addItem(self, num):
        position = bisect_left(self.items, num)
        self.items.insert(position, num)
        return self.median()

    def remItem(self, num):
        position = bisect_left(self.items, num)
        if (position >= len(self.items) or self.items[position] != num):
            return "Wrong!"
        else:
            del (self.items[position])
            return self.median()

    def median(self):
        l = len(self.items)
        if (l == 0):
            return "Wrong!"
        elif (l & 1):
            return self.items[int(l / 2)]
        else:
            ans = self.items[int(l / 2)] + self.items[int(l / 2) - 1]
            if (ans == 0):
                return 0
            elif (ans & 1):
                return ans / 2
            else:
                return int(ans / 2)


N = int(input())
arr = MedianFinder()
for i in range(N):
    Q = input().split(" ")
    num = int(Q[1])
    if (Q[0] == "a"):
        print(arr.addItem(num))
    elif (Q[0] == "r"):
        print(arr.remItem(num))