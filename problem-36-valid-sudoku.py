from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows

        def check_no_reps(a):
            filled = [x for x in a if x != '.']
            return len(filled) == len(set(filled))

        # check rows
        for row in board:
            if not check_no_reps(row):
                return False

        # check cols
        for col in range(9):
            values = [board[row][col] for row in range(9)]
            if not check_no_reps(values):
                return False

        # check rectangles
        for rect_start_row in range(0, 9, 3):
            for rect_start_col in range(0, 9, 3):
                values = []
                for row in range(3):
                    for col in range(3):
                        values.append(board[rect_start_row + row][rect_start_col + col])

                if not check_no_reps(values):
                    return False

        return True


if __name__ == '__main__':
    x = Solution()
    assert x.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )

    assert not x.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )
