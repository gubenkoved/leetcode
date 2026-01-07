from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def ray_sum(r, c, dr, dc):
            result = 0
            for d in range(3):
                result += grid[r][c]
                r += dr
                c += dc
            return result

        def is_magic(r, c):
            # check for same sum for rows and cols
            t = ray_sum(r, c, 0, +1)

            for d in range(3):
                if ray_sum(r + d, c, 0, +1) != t:
                    return False
                if ray_sum(r, c + d, +1, 0) != t:
                    return False

            # diagonals
            if ray_sum(r, c, +1, +1) != t:
                return False

            if ray_sum(r, c + 2, +1, -1) != t:
                return False

            # unique
            unique = set()
            for dr in range(3):
                for dc in range(3):
                    unique.add(grid[r + dr][c + dc])

                    if grid[r + dr][c + dc] > 9 or grid[r + dr][c + dc] <= 0:
                        return False

            if len(unique) != 9:
                return False

            return True

        for row in range(rows - 3 + 1):
            for col in range(cols - 3 + 1):
                if is_magic(row, col):
                    count += 1

        return count
