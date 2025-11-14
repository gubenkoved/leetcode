from typing import List


class Solution:
    # query[i] = [row1i, col1i, row2i, col2i]
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                A[r][c1] += 1
                if c2 + 1 < n:
                    A[r][c2 + 1] -= 1

        for r in range(n):
            for c in range(n):
                if c > 0:
                    A[r][c] += A[r][c - 1]

        return A


if __name__ == '__main__':
    x = Solution()
    print(x.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))
