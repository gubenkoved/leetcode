from typing import List
import itertools


class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}  # char -> Node
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def ensure(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                node = Node(char)
                cur.children[char] = node
            cur = cur.children[char]
        cur.eow = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # pre-process words into trie
        trie = Trie()

        for word in words:
            trie.ensure(word)

        found = set()

        # run search from all the cells
        n, m = len(board), len(board[0])

        def search(row, col, trie_node, cur, visited):
            if trie_node.eow:
                found.add(cur)

            candidates = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]

            for candidate_row, candidate_col in candidates:
                if candidate_row < 0 or candidate_row >= n:
                    continue
                if candidate_col < 0 or candidate_col >= m:
                    continue

                if (candidate_row, candidate_col) in visited:
                    continue

                candidate_char = board[candidate_row][candidate_col]
                if candidate_char in trie_node.children:
                    search(
                        candidate_row,
                        candidate_col,
                        trie_node.children[candidate_char],
                        cur + candidate_char,
                        set(itertools.chain(visited, [(candidate_row, candidate_col)])))

        for row in range(n):
            for col in range(m):
                char = board[row][col]
                if char in trie.root.children:
                    search(row, col, trie.root.children[char], char, {(row, col)})

        return list(found)


if __name__ == '__main__':
    x = Solution()
    print(
        x.findWords(
            board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            words=["oath", "pea", "eat", "rain"]))
