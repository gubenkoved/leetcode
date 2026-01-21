from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # instead of calculating every time we can calculate prefix sums
        # and then all the range sums will be calculated in O(1)
        def ray_sum(r, c, s, dr, dc):
            res = 0
            for _ in range(s):
                res += grid[r][c]
                r += dr
                c += dc
            return res

        def check(r, c, s):
            # start with canonical target
            target = ray_sum(r, c, s, +1, 0)

            # check all rows
            for d in range(s):
                if ray_sum(r + d, c, s, 0, +1) != target:
                    return False

            # check all cols
            for d in range(s):
                if ray_sum(r, c + d, s, +1, 0) != target:
                    return False

            # check diagonals
            if ray_sum(r, c, s, +1, +1) != target:
                return False

            if ray_sum(r, c + s - 1, s, +1, -1) != target:
                return False

            return True

        result = 0

        for r in range(rows):
            for c in range(cols):
                for s in range(1, min(rows, cols) + 1):
                    if r + s > rows or c + s > cols:
                        continue
                    if check(r, c, s):
                        result = max(result, s)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.largestMagicSquare([[1]]), 1)
