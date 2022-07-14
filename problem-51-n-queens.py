# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

from typing import List, Set, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        found = []

        # field there uses 2D array filled with bool where True means taken cell
        # field is a list of coordinates of placed queens
        def find(placed: List[Tuple[int, int]], taken_cols: Set[int], row: int):
            if row == n:
                # found!
                found.append([
                    '.' * max(0, c) + 'Q' + '.' * max(0, n - c - 1)
                    for _, c in placed
                ])

            # place rows-th queen
            for col in range(n):
                if col in taken_cols:
                    continue

                # check against diagonals
                beaten = False
                for x, y in placed:
                    dx = row - x
                    dy = col - y
                    if abs(dx) == abs(dy):
                        beaten = True
                        break

                if beaten:
                    continue

                # lets go deeper!
                taken_cols.add(col)
                placed.append((row, col))
                find(placed, taken_cols, row + 1)
                placed.pop(-1)
                taken_cols.discard(col)

        find([], set(), 0)

        return found


if __name__ == '__main__':
    x = Solution()
    print(x.solveNQueens(4))
