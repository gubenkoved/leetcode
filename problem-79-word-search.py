from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        # volatile state
        taken = set()

        def find(row, col):
            if len(taken) == len(word):
                return True

            adjacent = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1)
            ]

            target = word[len(taken)]

            for next_row, next_col in adjacent:
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                next_point = (next_row, next_col)

                if next_point in taken:
                    continue

                if board[next_row][next_col] == target:
                    taken.add(next_point)
                    sub_result = find(next_row, next_col)
                    if sub_result:
                        return True
                    taken.discard(next_point)

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    taken = {(row, col)}
                    if find(row, col):
                        return True
        return False


if __name__ == '__main__':
    x = Solution()
    print(x.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
    print(x.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
