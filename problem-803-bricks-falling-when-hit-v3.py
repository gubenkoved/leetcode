import time
from collections import deque
from copy import deepcopy
from typing import List


# the idea which is not mine:
# trace backwards, start with the end grid with all the hits applied
# and for each step we have to count how many new blocks added to the
# island connected to the top row


class DisjointSet:
    def __init__(self):
        self.parents = dict()
        self.root_size = dict()

    def ensure(self, x):
        if x in self.parents:
            return

        self.parents[x] = x
        self.root_size[x] = 1

    def component_size(self, x):
        assert x in self.parents
        root = self.find(x)
        return self.root_size[root]

    # returns root for the given item
    def find(self, x):
        cur = self.parents[x]

        while cur != self.parents[cur]:
            cur = self.parents[cur]

        # optimize the traversal for next time -> shortcut to the root
        self.parents[x] = cur

        return cur

    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # x root will be new root for y_root
        self.parents[y_root] = x_root
        self.root_size[x_root] += self.root_size.pop(y_root)


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        result = []
        n, m = len(grid), len(grid[0])

        # apply all the hits to the grid
        # use special marker "-1" to mark the places in the grid which are empty,
        # so there is nothing to erase from there
        for row, col in hits:
            if grid[row][col] == 1:
                grid[row][col] = 0
            else:
                grid[row][col] = -1

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m

        def neighbors(row, col):
            return [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]

        def dfs(row, col, visited):
            if (row, col) in visited:
                return

            visited.add((row, col))

            for row2, col2 in neighbors(row, col):
                if not is_valid(row2, col2):
                    continue

                if grid[row2][col2] != 1:
                    continue

                dfs(row2, col2, visited)

        # root for the items which are connected to the top row (and so stable)
        stable_root = None
        djs = DisjointSet()
        visited = set()
        for row in range(n):
            for col in range(m):
                if grid[row][col] != 1:
                    continue
                root = (row, col)
                if root in visited:
                    continue
                djs.ensure(root)
                if row == 0:
                    if stable_root is not None:
                        djs.merge(stable_root, root)
                    else:
                        stable_root = root
                traversed = set()
                dfs(row, col, traversed)
                visited.update(traversed)
                for row2, col2 in traversed:
                    djs.ensure((row2, col2))
                    djs.merge(root, (row2, col2))

        # trace backwards starting from the last hit and count how many bricks in
        # the block connected to the top row
        for row, col in reversed(hits):
            if grid[row][col] == -1:
                result.append(0)
                continue

            # assert grid[row][col] != 1
            grid[row][col] = 1

            cur = (row, col)
            djs.ensure(cur)

            stable_size_before = djs.root_size[stable_root] if stable_root is not None else 0

            if row == 0:
                if stable_root is not None:
                    djs.merge(stable_root, cur)
                else:
                    stable_root = cur

            for row2, col2 in neighbors(row, col):
                if not is_valid(row2, col2):
                    continue
                if grid[row2][col2] != 1:
                    continue
                djs.merge((row2, col2), cur)

            # fix stable root if changed
            if stable_root is not None:
                stable_root = djs.find(stable_root)

            stable_size_after = djs.root_size[stable_root] if stable_root is not None else 0

            # stable size did not change -> 0
            # stable size increased by 1 -> we just added hit brick -> 0 fallen
            # stable size increased by N -> N - 1 fallen
            result.append(max(0, stable_size_after - stable_size_before - 1))

        return list(reversed(result))


if __name__ == '__main__':
    x = Solution()
    print(x.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], hits=[[1, 0]]))
    print(x.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], hits=[[1, 1], [1, 0]]))
    print(x.hitBricks([[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]))
    print(x.hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]))
    print(x.hitBricks([[0, 1, 1, 1, 1],   # 0
                       [1, 1, 1, 1, 0],   # 1
                       [1, 1, 1, 1, 0],   # 2
                       [0, 0, 1, 1, 0],   # 3
                       [0, 0, 1, 0, 0],   # 4
                       [0, 0, 1, 0, 0],   # 5
                       [0, 0, 0, 0, 0],   # 6
                       [0, 0, 0, 0, 0],   # 7
                       [0, 0, 0, 0, 0]],  # 8
                      hits=[[6, 0], [1, 0], [4, 3], [1, 2], [7, 1], [6, 3], [5, 2], [5, 1], [2, 4], [4, 4], [7, 3]]))
    print(x.hitBricks([[1, 0, 1],
                       [1, 1, 1]],
                      hits=[[0, 0], [0, 2], [1, 1]]))

    with open('input2.txt') as f:
        bricks = eval(f.readline())
        hits = eval(f.readline())
        print(x.hitBricks(bricks, hits))
