from typing import List

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        idx = 1
        cur_x, cur_y = 0, 0

        # go all the way to the right
        for _ in range(n):
            matrix[cur_y][cur_x] = idx
            cur_x += 1
            idx += 1

        # now go in two directions with k steps,
        # then decrease step by 1, repeat till the step size is zero,
        # or idx is equal to n ** 2
        k = n - 1

        direction = 1
        cur_x -= 1

        m = {
            0: (+1, 0),  # right
            1: (0, +1),  # down
            2: (-1, 0),  # left
            3: (0, -1),  # up
        }

        def move():
            nonlocal cur_x
            nonlocal cur_y
            nonlocal idx
            dx, dy = m[direction]
            cur_x, cur_y = cur_x + dx, cur_y + dy
            matrix[cur_y][cur_x] = idx
            idx += 1

        while k != 0:

            for _ in range(k):
                move()

            direction = (direction + 1) % 4

            for _ in range(k):
                move()

            direction = (direction + 1) % 4
            k -= 1

        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
