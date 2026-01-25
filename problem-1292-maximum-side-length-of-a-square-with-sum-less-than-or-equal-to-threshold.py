from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        rows, cols = len(mat), len(mat[0])

        # cumulative sums
        sums = [[0 for _ in range(cols)] for _ in range(rows)]

        def cum_sum(r, c):
            if r < 0:
                return 0
            if c < 0:
                return 0
            return sums[r][c]

        # fill the sums!
        for r in range(rows):
            for c in range(cols):
                sums[r][c] = mat[r][c] + cum_sum(r - 1, c) + cum_sum(r, c - 1) - cum_sum(r - 1, c - 1)

        def sq_sum(r, c, s):
            return (
                cum_sum(r + s - 1, c + s - 1)
                - cum_sum(r - 1, c + s - 1)
                - cum_sum(r + s - 1, c - 1)
                + cum_sum(r - 1, c - 1)
            )

        result = 0

        for r in range(rows):
            for c in range(cols):
                max_size = min(rows - r, cols - c)
                for s in range(result, max_size + 1):
                    if sq_sum(r, c, s) <= threshold:
                        result = max(result, s)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4), 2)
    # print(x.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1), 0)
    print(x.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold=40184), 2)
