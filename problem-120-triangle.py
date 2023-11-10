from typing import List
from functools import lru_cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        @lru_cache(maxsize=None)
        def min_path_sum(row, col):
            if row == rows - 1:
                return triangle[row][col]

            return min(
                min_path_sum(row + 1, col),
                min_path_sum(row + 1, col + 1)
            ) + triangle[row][col]

        return min_path_sum(0, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
