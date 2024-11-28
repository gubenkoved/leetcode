from typing import List
import heapq


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # basically just a simple dijkstra with wall costing 1 and no wall being free of charge
        visited = set()
        # (cost, x, y)
        heap = [(0, 0, 0)]
        m, n = len(grid), len(grid[0])

        while heap:
            cost, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if x == m - 1 and y == n - 1:
                return cost

            candidates = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ]
            for x2, y2 in candidates:
                if x2 < 0 or x2 >= m:
                    continue
                if y2 < 0 or y2 >= n:
                    continue
                cost2 = cost + grid[x2][y2]
                heapq.heappush(heap, (cost2, x2, y2))

        assert False


if __name__ == '__main__':
    x = Solution()
    print(x.minimumObstacles([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]]))