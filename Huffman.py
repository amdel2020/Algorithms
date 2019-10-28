from collections import defaultdict
from queue import PriorityQueue

class Node:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

class HuffmanEncoding:

    def encode(self, root, string, huffmanCode):
        if root is None:
            return

        if root.left is None and root.right is None:
            huffmanCode[root.char] = string

        self.encode(root.left, string + '0', huffmanCode)
        self.encode(root.right, string + '1', huffmanCode)

    def buildHuffman(self, text):
        freq = defaultdict(int)
        pq = PriorityQueue(len(text))

        for ch in text:
            freq[ch] += 1

        for k, v in freq.items():
            n = Node(k, v)
            pq.put((v, Node(k, v)))

        while len(pq) > 1:
            left = pq.get()
            right = pq.get()
            s = left[0] + right[0]
            newNode = Node('\0', s, left, right)

        huffmanCode = defaultdict(str)
        self.encode(pq[0][1])

        for k, v in huffmanCode:
            print(k + ": " + v)


text = "Huffman coding is a data compression algorithm"
h = HuffmanEncoding()
h.buildHuffman(text)
