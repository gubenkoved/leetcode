from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue

                val = 1 if row == 0 and col == 0 else 0

                if col > 0:
                    val += dp[row][col-1]

                if row > 0:
                    val += dp[row-1][col]

                dp[row][col] = val

        return dp[rows - 1][cols - 1]


if __name__ == '__main__':
    x = Solution()
    assert x.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
