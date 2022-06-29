from typing import List

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # print(f'{rows}x{cols}')

        # contains sum of all cells starting from left top corner and ends with
        # current cell
        sums = [[0] * cols for _ in range(rows)]

        def get_sum(r, c):
            if r < 0:
                return 0
            if c < 0:
                return 0
            return sums[r][c]

        for r in range(rows):
            for c in range(cols):
                v = get_sum(r - 1, c) + get_sum(r, c - 1) - get_sum(r - 1, c - 1)
                if matrix[r][c] == "1":
                    v += 1
                sums[r][c] = v

        # print('sums calculated')
        # print(sums)
        best_sum = 0

        for start_row in range(rows):
            # print(f'handle row {start_row}')
            for start_col in range(cols):
                if matrix[start_row][start_col] != "1":
                    continue

                max_possible_size = (rows - start_row) * (cols - start_col)
                if best_sum >= max_possible_size:
                    break

                for end_row in range(start_row, rows):
                    if matrix[end_row][start_col] != "1":
                        break
                    for end_col in range(start_col, cols):
                        if matrix[end_row][end_col] != "1":
                            break

                        expected_sum = (end_row - start_row + 1) * (end_col - start_col + 1)

                        if best_sum >= expected_sum:
                            continue

                        cur_sum = (
                                sums[end_row][end_col] -
                                get_sum(end_row, start_col - 1) -
                                get_sum(start_row - 1, end_col) +
                                get_sum(start_row - 1, start_col - 1)
                        )

                        if expected_sum == cur_sum:
                            if cur_sum > best_sum:
                                print(f'new max rect of size {cur_sum}: ({start_row}, {start_col}) to ({end_row}, {end_col})')
                                best_sum = cur_sum
                        else:
                            break  # no need to enlarge it further

        return best_sum


if __name__ == '__main__':
    x = Solution()
    # print(x.maximalRectangle(
    #     [["1", "0", "1", "0", "0"],
    #      ["1", "0", "1", "1", "1"],
    #      ["1", "1", "1", "1", "1"],
    #      ["1", "0", "0", "1", "0"]]
    # ))
    # f = open('input.txt')
    # matrix = eval(f.read())
    # matrix = [["1"] * 200 for _ in range(200)]
    # print(x.maximalRectangle(matrix))
    # print(x.maximalRectangle([["1"]]))
