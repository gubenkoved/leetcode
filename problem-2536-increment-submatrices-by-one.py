from typing import List


class Solution:
    # query[i] = [row1i, col1i, row2i, col2i]
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # delta[r][c] will drive the delta for the prefix sum as scanned
        # from left to right
        deltas = [[0] * n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                deltas[r][c1] += 1
                if c2 + 1 < n:
                    deltas[r][c2 + 1] -= 1

        prefix_sums = [[0] * n for _ in range(n)]

        for r in range(n):
            val = 0
            for c in range(n):
                val += deltas[r][c]
                prefix_sums[r][c] = val

        # now we can compute the result
        return prefix_sums


if __name__ == '__main__':
    x = Solution()
    print(x.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))
