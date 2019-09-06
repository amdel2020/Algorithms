# construct trie
# if trie not constructed and u found end of word, then u found prefix
# elif trie is constructed fully, but end of word node still have more children or already end of word, then prefix

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

    def insert(self, word):
        node = self
        for w in word:
            node = node.children[w]
            if node.isEnd:
                return False

        if node.isEnd or len(node.children) > 0:
            return False

        node.isEnd = True
        return True


if __name__ == "__main__":
    n = int(input())
    trie = TrieNode()
    flag = True
    cul = ''

    for i in range(n):
        s = input().strip()
        if not trie.insert(s):
            flag = False
            cul = s
            break

    if flag:
        print("GOOD SET")
    else:
        print("BAD SET")
        print(cul)
