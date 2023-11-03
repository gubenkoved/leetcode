from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we will be processing board in-place row by row, column by column, and
        # mark as follows processed cells:
        #
        # > 0 means that cell is dead and stays dead
        # > 1 means that cell is alive and stays alive
        # > 2 means that cell was dead, but is alive on the next round
        # > 3 means that cell was alive but will be dead in the next round
        #
        # after we processed whole board
        rows, cols = len(board), len(board[0])

        def count_alive(row, col):
            count = 0
            for row_d in range(-1, 2):
                for col_d in range(-1, 2):
                    if row_d == 0 and col_d == 0:
                        continue

                    if row + row_d < 0 or row + row_d >= rows:
                        continue

                    if col + col_d < 0 or col + col_d >= cols:
                        continue

                    if board[row + row_d][col + col_d] in [1, 3]:
                        count += 1
            return count

        # pass 1: computation round
        for row in range(rows):
            for col in range(cols):
                c = count_alive(row, col)
                result = None

                if board[row][col] == 1:
                    # currently alive cell
                    if c < 2:
                        result = 3  # dying
                    elif c <= 3:
                        result = 1  # stays alive
                    else:
                        # overpopulation
                        result = 3
                else:  # currently dead cell
                    if c == 3:
                        result = 2  # new alive cell is born!
                    else:
                        result = 0  # stays dead

                assert result is not None

                board[row][col] = result

        # pass 2: replacement
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 3:
                    board[row][col] = 0


if __name__ == '__main__':
    x = Solution()


    def check(s, expected):
        print(s)
        x.gameOfLife(s)
        print(s)
        assert s == expected


    check([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
    check([[1, 1], [1, 0]], [[1, 1], [1, 1]])
    check([[0, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 0]],
          [[1, 1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0]])
