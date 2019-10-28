class MinHeap:
    def __init__(self, collection=None):
        self._heap = []

        if collection is not None:
            for item in collection:
                self.push(item)

    def push(self, item):
        self._heap.append(item)
        self._shiftUp(len(self._heap))

    def extractMin(self):
        self._swap(0, len(self._heap)-1)
        res = self._heap.pop()
        self._shiftDown(self, 0)
        return res

    def _shiftUp(self, idx):
        parentIdx = (idx-1)//2

        if parentIdx < 0:
            return

        if self._heap[parentIdx] < self._heap[idx]:
            self._swap(parentIdx], idx)
            self._shiftUp(parentIdx)

    def _shiftDown(self, idx):
        childIdx = 2*idx+1

        if childIdx > len(self._heap):
            return

        if childIdx+1 < len(self._heap) and self._heap[childIdx+1] < self._heap[childIdx]:
            childIdx += 1

        if self._heap[childIdx] > self._heap[idx]:
            self._swap(childIdx, idx)
            self._shiftDown(childIdx)

    def _swap(x, y):
        self._heap[x], self._heap[y] = self._heap[y], self._heap[x]
