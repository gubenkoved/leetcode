from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])

        heap = []
        visited = set()

        # (time, row, col)
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return t

            adjacent = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            for nr, nc in adjacent:
                if not (0 <= nr < rows) or not (0 <= nc < cols):
                    continue

                nt = max(moveTime[nr][nc], t) + 1
                heapq.heappush(heap, (nt, nr, nc))

        return -1


if __name__ == '__main__':
    x = Solution()
    print(x.minTimeToReach([[0,4],[4,4]]))
