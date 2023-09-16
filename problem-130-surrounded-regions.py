from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])

        def walk(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            visited = set()
            is_anchored = False

            while queue:
                row, col = queue.popleft()

                if (row, col) in visited:
                    continue

                visited.add((row, col))

                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    is_anchored = True

                neighbors = [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]

                for next_row, next_col in neighbors:
                    if next_row < 0 or next_row >= rows:
                        continue
                    if next_col < 0 or next_col >= cols:
                        continue
                    if board[next_row][next_col] != 'O':
                        continue

                    queue.append((next_row, next_col))

            return is_anchored, visited

        global_visited = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    if (row, col) in global_visited:
                        continue

                    is_anchored, visited = walk(row, col)

                    global_visited.update(visited)

                    if not is_anchored:
                        for r, c in visited:
                            board[r][c] = 'X'
