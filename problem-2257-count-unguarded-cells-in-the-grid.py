from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        state = [[''] * n for _ in range(m)]

        def scan(row, col, row_delta, col_delta, is_guarded):
            while True:
                if state[row][col] == 'G':
                    is_guarded = True
                elif state[row][col] == 'W':
                    is_guarded = False
                elif is_guarded:
                    # capture that state is guarded
                    state[row][col] = 'g'

                # move to the next cell
                row += row_delta
                col += col_delta

                if row < 0 or row >= m or col < 0 or col >= n:
                    break

        # place guards and walls
        for r, c in guards:
            state[r][c] = 'G'

        for r, c in walls:
            state[r][c] = 'W'

        # scan in all directions
        for row in range(m):
            scan(row, 0, 0, +1, False)
            scan(row, n - 1, 0, -1, False)

        for col in range(n):
            scan(0, col, +1, 0, False)
            scan(m - 1, col, -1, 0, False)

        # now count of updated state
        result = 0
        for row in range(m):
            for col in range(n):
                if state[row][col] == '':
                    result += 1
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]), 7)
