import collections
import heapq
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        teleport_targets = collections.defaultdict(list)

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):

                for r2 in range(rows):
                    for c2 in range(cols):

                        if r2 == r and c2 == c:
                            continue

                        if grid[r2][c2] <= grid[r][c]:
                            teleport_targets[(r, c)].append((r2, c2))

        heap = [
            # (cost, -teleports left, (r, c), )
            (0, -k, (0, 0)),
        ]

        visited = set()

        finish = (rows - 1, cols - 1)

        while heap:
            cost, k_left_neg, pos = heapq.heappop(heap)

            if pos in visited:
                continue

            visited.add(pos)

            if pos == finish:
                return cost

            r, c = pos

            candidates = [
                (r + 1, c),
                (r, c + 1),
            ]

            for nr, nc in candidates:
                if nr >= rows or nc >= cols:
                    continue
                if (nr, nc) not in visited:
                    heapq.heappush(heap, (cost + grid[nr][nc], k_left_neg, (nr, nc)))

            # tele-neighbors
            if k_left_neg < 0:
                for nr, nc in teleport_targets[(r,c)]:
                    if (nr, nc) not in visited:
                        heapq.heappush(heap, (cost, k_left_neg + 1, (nr, nc)))

        assert False, 'unreachable'


if __name__ == '__main__':
    x = Solution()
    print(x.minCost([[6, 7, 1,  20, 11],
                     [4, 5, 18, 23, 28]], 3), 46)

    print(x.minCost([[9, 2, 7, 9,17,11,6, 23,24],
                     [17,10,19,8,19,18,27,16,23]], 2), 23)

    print(x.minCost([[19,10],[23,13],[16,32],[38,41],[30,36],[53,31]], 1), 55)