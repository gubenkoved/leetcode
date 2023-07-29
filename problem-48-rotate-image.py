from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def swap(p1, p2):
            tmp = matrix[p1[0]][p1[1]]
            matrix[p1[0]][p1[1]] = matrix[p2[0]][p2[1]]
            matrix[p2[0]][p2[1]] = tmp

        n = len(matrix)
        for row in range(0, n // 2):
            for col in range(row, n - 1 - row):
                # print('rotate at (%s, %s)' % (row, col))
                swap((row, col), (n - col - 1, row))
                swap((n - col - 1, row), (n - row - 1, n - col - 1))
                swap((n - row - 1, n - col - 1), (col, n - row - 1))


if __name__ == '__main__':
    x = Solution()


    def case(arr):
        x.rotate(arr)
        for line in arr:
            print(line)
        print()


    case([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    case([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
