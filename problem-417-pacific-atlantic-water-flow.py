from typing import List
from functools import cache


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        @cache
        def neighbors(r, c):
            candidates = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            result = []
            for nr, nc in candidates:
                if not is_valid(nr, nc):
                    continue
                # NOTE: criteria is reversed -> we are never going DOWNstream
                if heights[nr][nc] < heights[r][c]:
                    continue
                result.append((nr, nc))
            return result

        # we will reverse the processing a bit -- will start from shores of the
        # oceans and mark reachable cells

        visited = set()

        def trace(cell):
            if cell in visited:
                return
            visited.add(cell)
            for n_cell in neighbors(*cell):
                trace(n_cell)
            pass

        # handle pacific
        for c in range(cols):
            trace((0, c))

        for r in range(rows):
            trace((r, 0))

        cells_with_pacific_reachable = visited
        visited = set()

        # handle atlantic
        for c in range(cols):
            trace((rows - 1, c))

        for r in range(rows):
            trace((r, cols - 1))

        cells_with_atlantic_reachable = visited

        result = []
        for r in range(rows):
            for c in range(cols):
                cell = (r, c)
                if cell in cells_with_pacific_reachable and cell in cells_with_atlantic_reachable:
                    result.append(cell)

        return result

if __name__ == '__main__':
    x = Solution()
    # print(x.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(x.pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]), [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]])
