# Given an m x n matrix, return all elements of the matrix in spiral order.
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)

        min_x, max_x = 0, width - 1
        min_y, max_y = 1, height - 1

        if width > 1:
            direction = 0
        else:
            direction = 1

        # 0 - right
        # 1 - down
        # 2 - left
        # 3 - up

        result = []

        cur_x, cur_y = 0, 0
        for _ in range(width * height):
            result.append(matrix[cur_y][cur_x])

            if direction == 0:
                cur_x += 1

                if cur_x == max_x:
                    max_x -= 1
                    direction += 1
            elif direction == 1:
                cur_y += 1

                if cur_y == max_y:
                    max_y -= 1
                    direction += 1
            elif direction == 2:
                cur_x -= 1

                if cur_x == min_x:
                    min_x += 1
                    direction += 1
            else:
                cur_y -= 1

                if cur_y == min_y:
                    min_y += 1
                    direction = 0

        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.spiralOrder([
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    # ]))
    # print(s.spiralOrder([
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]))
    print(s.spiralOrder([
        [1],
        [2],
        [3]
    ]))
    print(s.spiralOrder([
        [1, 2, 3],
    ]))
