from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        # partial sums
        p = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                val = int(matrix[i][j])

                if i != 0:
                    val += int(p[i - 1][j])

                if j != 0:
                    val += int(p[i][j - 1])

                if i != 0 and j != 0:
                    val -= int(p[i - 1][j - 1])

                p[i][j] = val

        best_size = 0

        def pf(i, j):
            if i < 0 or j < 0:
                return 0
            return p[i][j]

        # now calculate the answer
        for size in range(1, min(n, m) + 1):
            go_to_next_size = False

            for i in range(n - size + 1):
                if go_to_next_size:
                    break

                for j in range(m - size + 1):
                    actual_sum = (
                            p[i + size - 1][j + size - 1]
                            - pf(i + size - 1, j - 1)
                            - pf(i - 1, j + size - 1)
                            + pf(i - 1, j - 1)
                    )

                    if actual_sum == size ** 2:
                        best_size = size
                        go_to_next_size = True
                        break

        return best_size ** 2


if __name__ == '__main__':
    x = Solution()
    assert x.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]) == 4
