from typing import Optional


class Node:
    def __init__(self, char):
        self.char = char
        self.child_map = {}
        self.eow = False  # end of word


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        prev = self.head

        for idx in range(len(word)):
            c = word[idx]

            if c in prev.child_map:
                prev = prev.child_map[c]
            else:
                node = Node(c)
                prev.child_map[c] = node
                prev = node

        prev.eow = True

    def _walk(self, prefix: str) -> Optional[Node]:
        if self.head is None:
            return None

        prev = self.head

        for idx in range(len(prefix)):
            c = prefix[idx]
            prev = prev.child_map.get(c)

            if prev is None:
                return None

        return prev

    def search(self, word: str) -> bool:
        if not word:
            return True

        node = self._walk(word)

        return node and node.eow

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        node = self._walk(prefix)

        return node is not None


if __name__ == '__main__':
    x = Trie()
    x.insert('apple')
    print(x.search('apple'))
