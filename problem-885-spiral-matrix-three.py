from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        traversed = 0
        result = []

        col, row = cStart, rStart

        result.append((row, col))
        traversed += 1

        direction = 0

        delta = {
            0: (+1, 0),  # east
            1: (0, +1),  # south
            2: (-1, 0),  # west
            3: (0, -1),  # north
        }

        def go():
            nonlocal traversed
            nonlocal col
            nonlocal row
            delta_col, delta_row = delta[direction]
            col += delta_col
            row += delta_row

            if 0 <= col < cols and 0 <= row < rows:
                traversed += 1
                result.append((row, col))

        k = 1

        while traversed < rows * cols:

            for _ in range(k):
                go()

            direction = (direction + 1) % 4

            for _ in range(k):
                go()

            direction = (direction + 1) % 4

            k += 1

        return result


if __name__ == '__main__':
    print(Solution().spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4))
