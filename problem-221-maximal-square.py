from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        # dp[i][j] is maximal size of square that ends at (i, j) that is
        # fully filled with "1"
        dp = [[0] * m for _ in range(n)]

        best = 0
        for row in range(n):
            for col in range(m):

                if matrix[row][col] == "0":
                    continue

                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col])
                else:
                    dp[row][col] = min(
                        int(dp[row - 1][col]),
                        int(dp[row][col - 1]),
                        int(dp[row - 1][col - 1])
                    ) + 1

                best = max(best, int(dp[row][col]))

        return best ** 2


if __name__ == '__main__':
    x = Solution()
    assert x.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]) == 4
