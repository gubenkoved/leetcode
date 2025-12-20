from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # heap of (level, (r, c))
        heap = []

        rows = len(heightMap)
        cols = len(heightMap[0])

        for r in range(rows):
            heapq.heappush(heap, (heightMap[r][0], (r, 0)))
            heapq.heappush(heap, (heightMap[r][cols - 1], (r, cols - 1)))

        for c in range(cols):
            heapq.heappush(heap, (heightMap[0][c], (0, c)))
            heapq.heappush(heap, (heightMap[rows - 1][c], (rows - 1, c)))

        trapped = 0
        visited = set()

        # now trace using the smallest level as it would be draining from neighbor
        # all other cells are higher, so at each cell we trap amount equal

        while heap:
            level, (r, c) = heapq.heappop(heap)

            if (r,c) in visited:
                continue

            visited.add((r, c))

            trapped += max(0, level - heightMap[r][c])

            neigh = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            for nr, nc in neigh:
                if nr < 0 or nr >= rows:
                    continue
                if nc < 0 or nc >= cols:
                    continue
                heapq.heappush(heap, (max(level, heightMap[r][c]), (nr, nc)))

        return trapped

if __name__ == '__main__':
    x = Solution()
    print(x.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]), 4)
