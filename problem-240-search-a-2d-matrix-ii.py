from typing import List
from bisect import bisect_left


class Solution:
    # O(n * logm)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        for row in range(n):
            idx = bisect_left(matrix[row], target)
            if idx < m and matrix[row][idx] == target:
                return True
        return False


if __name__ == '__main__':
    x = Solution()
    print(x.searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=5))
    print(x.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
