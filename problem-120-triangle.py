from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        # note that allowed range for values is -10^4 <= x <= 10^4
        # we will use original array to hold intermediary results to
        # cover follow-up requirements of using only O(rows) extra memory
        # max triangle size is 200, so sum should be:
        # -2 * 10^6 <= sum <= 2 * 10^6

        # if value is bigger than M, then we know it is not original one, but
        # result of our processing
        M = 10 ** 4
        OFFSET = 200 * M + 1

        def min_path_sum(row, col):
            if row == rows - 1:
                return triangle[row][col]

            # this is how we simulate our cache using original array to store
            if triangle[row][col] > M:
                return triangle[row][col] - OFFSET

            val = min(
                min_path_sum(row + 1, col),
                min_path_sum(row + 1, col + 1)
            ) + triangle[row][col]

            triangle[row][col] = val + OFFSET

            return val

        return min_path_sum(0, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
