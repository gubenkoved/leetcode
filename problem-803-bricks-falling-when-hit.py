from typing import List, Tuple, Set
from copy import deepcopy
from collections import deque
import sys


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        grid = deepcopy(grid)
        m, n = len(grid), len(grid[0])

        # walks from given start point, returns bool indicating
        # that top is reachable, so that it is stable
        def walk(r, c, visited):
            if (r, c) in visited:
                return
            if r == 0:
                return True
            visited.add((r, c))
            neighbors = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]
            for r2, c2 in neighbors:
                if r2 < 0 or r2 >= m:
                    continue
                if c2 < 0 or c2 >= n:
                    continue
                if grid[r2][c2] != 1:
                    continue
                nested_is_stable = walk(r2, c2, visited)
                if nested_is_stable:
                    return True
            return False

        result = []

        for r, c in hits:
            if grid[r][c] == 0:
                result.append(0)
                continue

            grid[r][c] = 0

            # when we remove a brick there are up to 4 "islands" formed, and
            # up to 3 "islands" will become no longer stable, so what we have to do
            # is to check to all 4 directions if given "island" is stable or not
            neighbors = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            fallen = set()
            for r2, c2 in neighbors:
                if r2 < 0 or r2 >= m:
                    continue
                if c2 < 0 or c2 >= n:
                    continue
                if grid[r2][c2] != 1:
                    continue

                # check the island!
                visited = set()
                is_stable = walk(r2, c2, visited)

                if not is_stable:
                    fallen.update(visited)

            # update the grid
            for r, c in fallen:
                grid[r][c] = 0

            result.append(len(fallen))

        return result


if __name__ == '__main__':
    sys.setrecursionlimit(200 * 200 + 100)
    x = Solution()
    # print(x.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], hits=[[1, 0]]))
    # print(x.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], hits=[[1, 1], [1, 0]]))
    # print(x.hitBricks([[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]))
    # print(x.hitBricks([[1,0,1], [1,1,1]], [[0,0],[0,2],[1,1]]))

    with open('input.txt') as f:
        bricks = eval(f.readline())
        hits = eval(f.readline())
        print(x.hitBricks(bricks, hits))
