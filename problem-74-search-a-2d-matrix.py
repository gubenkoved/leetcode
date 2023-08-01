from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # this is pretty much regular binary search over virtual 1D array that
        # corresponds to the row-by-row traversal over the original array
        rows = len(matrix)
        cols = len(matrix[0])

        def val(linear_idx):
            row = linear_idx // cols
            col = linear_idx % cols
            return matrix[row][col]

        def binary_find(left_incl, right_excl):
            if right_excl - left_incl == 1:
                if val(left_incl) == target:
                    return True
                else:
                    return False

            median_idx = (left_incl + right_excl) // 2
            median_val = val(median_idx)

            if median_val == target:
                return True
            elif median_val > target:
                return binary_find(left_incl, median_idx)
            else:
                return binary_find(median_idx, right_excl)

        return binary_find(0, rows * cols)


if __name__ == '__main__':
    x = Solution()
    print(x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))