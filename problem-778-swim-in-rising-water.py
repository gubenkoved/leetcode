from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [
            (grid[0][0], (0, 0))
        ]

        dist = {}

        while heap:
            t, (r, c) = heapq.heappop(heap)

            if (r, c) in dist:
                continue

            dist[(r, c)] = t

            neigh = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            for nr, nc in neigh:
                if nr < 0 or nr >= n:
                    continue
                if nc < 0 or nc >= n:
                    continue
                nt = max(t, grid[nr][nc])
                heapq.heappush(heap, (nt, (nr, nc)))

        return dist[(n-1, n-1)]
