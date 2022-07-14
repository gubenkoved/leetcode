from typing import List, Set, Tuple

class Solution:
    def totalNQueens(self, n: int) -> int:
        found = 0

        # field there uses 2D array filled with bool where True means taken cell
        # field is a list of coordinates of placed queens
        def find(placed: List[Tuple[int, int]], taken_cols: Set[int], row: int):
            nonlocal found

            if row == n:
                found += 1

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