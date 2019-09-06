class DisjointSet:
    def __init__(self, count):
        self.parent = [0] * count
        self.size_of_set = [1] * count

        for i in range(count):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] is i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_rep = self.find(i)
        j_rep = self.find(j)

        if i_rep == j_rep:
            return

        self.parent[i_rep] = j_rep
        self.size_of_set[j_rep] += self.size_of_set[i_rep]
        self.size_of_set[i_rep] = 0

    def min_max_component(self):
        low = len(self.parent)
        high = 0

        for i in range(1, len(self.parent)):
            if 1 < self.size_of_set[i] < low:
                low = self.size_of_set[i]
            high = max(high, self.size_of_set[i])

        return low, high


if __name__ == '__main__':
    n = 5
    disjoint_set = DisjointSet(2*n+1)
    disjoint_set.union(1, 6)
    disjoint_set.union(2, 7)
    disjoint_set.union(3, 8)
    disjoint_set.union(4, 9)
    disjoint_set.union(2, 6)

    min_c, max_c = disjoint_set.min_max_component()
    print(str(min_c) + ' ' + str(max_c))



