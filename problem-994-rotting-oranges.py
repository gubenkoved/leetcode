from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        queue = deque()  # (epoch, (row, col))

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    queue.append((0, (row, col)))

        rotten = set()
        visited = set()
        max_distance = 0

        while queue:
            cur_epoch, (cur_row, cur_col) = queue.popleft()

            visit_key = (cur_row, cur_col)
            if visit_key in visited:
                continue

            visited.add(visit_key)

            if grid[cur_row][cur_col] == 1:
                max_distance = max(max_distance, cur_epoch)
                rotten.add((cur_row, cur_col))

            candidates = [
                (cur_row - 1, cur_col),
                (cur_row + 1, cur_col),
                (cur_row, cur_col - 1),
                (cur_row, cur_col + 1),
            ]

            for candidate_row, candidate_col in candidates:
                if not 0 <= candidate_row < n or not 0 <= candidate_col < m:
                    continue
                if grid[candidate_row][candidate_col] == 1:
                    queue.append((cur_epoch + 1, (candidate_row, candidate_col)))

        # check if there are any fresh ones
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row, col) not in rotten:
                    return -1

        return max_distance


if __name__ == '__main__':
    x = Solution()
    print(x.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(x.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(x.orangesRotting([[0, 2]]))
