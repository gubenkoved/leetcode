from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def can_cross(day):
            flooded = set()

            for idx in range(day):
                r = cells[idx][0] - 1
                c = cells[idx][1] - 1
                # (r,c) are 0-based now
                flooded.add((r, c))

            # add all the top land cells
            queue = deque()
            visited = set()

            # add top land cells to start from
            for c in range(col):
                if (0, c) not in flooded:
                    queue.append((0, c))

            while queue:
                r, c = queue.popleft()

                if (r, c) in visited:
                    continue

                if r == row - 1:
                    return True

                visited.add((r, c))

                candidates = [
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ]

                for nr, nc in candidates:
                    if nr < 0 or nr >= row:
                        continue
                    if nc < 0 or nc >= col:
                        continue
                    if (nr, nc) in flooded:
                        continue
                    if (nr, nc) not in visited:
                        queue.append((nr, nc))

            return False

        # binary search day
        left_incl, right_excl = 0, len(cells) + 1

        while right_excl - left_incl > 1:
            mid = (right_excl + left_incl) // 2

            if can_cross(mid):
                left_incl = mid
            else:
                right_excl = mid

        return left_incl


if __name__ == '__main__':
    x = Solution()
    print(x.latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]), 2)
    print(x.latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]), 1)
