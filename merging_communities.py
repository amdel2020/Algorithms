class DisjointSet:
    def __init__(self, count):
        self.parent = [0] * count
        self.size_of_set = [1] * count  # Use this rank

        for i in range(count):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] is i:
            return i

        # compress tree and return
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_rep = self.find(i)
        j_rep = self.find(j)

        if i_rep == j_rep:
            return

        if self.size_of_set[i_rep] < self.size_of_set[j_rep]:
            self.parent[i_rep] = j_rep
            self.size_of_set[j_rep] += self.size_of_set[i_rep]

        else:
            self.parent[j_rep] = i_rep
            self.size_of_set[i_rep] += self.size_of_set[j_rep]

    def set_size(self, i):
        return self.size_of_set[self.find(i)]


if __name__ == '__main__':
    n, q = map(int, input().strip().split())
    disjoint_set = DisjointSet(n+1)

    for _ in range(q):
        query = input().strip().split()

        if query[0] == 'Q':
            print(disjoint_set.set_size(int(query[1])))
        elif query[0] == 'M':
            i = int(query[1])
            j = int(query[2])
            disjoint_set.union(i, j)



