from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        zero_cols = []
        zero_rows = []

        # go horizontally
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    break

        # go vertically
        for col in range(cols):
            for row in range(rows):
                if matrix[row][col] == 0:
                    zero_cols.append(col)
                    break

        # fill the zero rows
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0

        # fill the zero cols
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0


if __name__ == '__main__':
    x = Solution()


    def case(arr):
        x.setZeroes(arr)
        for line in arr:
            print(line)
        print()


    case([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
