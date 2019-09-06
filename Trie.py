from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

    def insert(self, word):
        node = self
        for w in word:
            node = node.children[w]
        node.isEnd = True

    def search(self, word):
        node = self

        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return 0
        # prefix match
        # traverse current node to all leaf nodes
        result = []
        self.traverse(node, list(word), result)
        return len(result)

    def traverse(self, root, prefix, result):
        if root.isEnd:
            result.append(prefix[:])

        for c,n in root.children.items():
            prefix.append(c)
            self.traverse(n, prefix, result)
            prefix.pop(-1)

if __name__ == "__main__":
    n = int(input())
    trie = TrieNode()

    for i in range(n):
        cmd, string = input().split()

        if cmd == 'add':
            trie.insert(string)
        elif cmd == 'find':
            print(trie.search(string))