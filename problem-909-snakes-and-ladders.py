from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # this is just a simple shortest path in the graph kind of the problem
        # that can be solved with the simple BFS, the most unusual part is the
        # conversion from this wierd board encoding schema to something simple

        # stage 1: convert the board encoding
        portals = {}  # source -> destination

        idx = 1
        n = len(board)
        row, col = n - 1, 0
        direction = 1  # 1 is right, 2 is up, 3 is left

        while idx != n * n:
            idx += 1

            if direction == 1:
                col += 1

                if col == n - 1:
                    direction = 2  # go up now!
            elif direction == 2:
                row -= 1

                if col == n - 1:
                    direction = 3
                else:
                    direction = 1
            elif direction == 3:
                col -= 1

                if col == 0:
                    direction = 2

            if board[row][col] != -1:
                portals[idx] = board[row][col]

        # stage 2: BFS
        visited = set()
        queue = deque()
        queue.append(1)
        distance = {}
        distance[1] = 0

        while queue:
            idx = queue.popleft()

            if idx in visited:
                continue

            visited.add(idx)

            for reachable in range(idx + 1, min(n * n + 1, idx + 1 + 6)):
                effective_destination = reachable

                # follow ladder or snake if any
                if effective_destination in portals:
                    effective_destination = portals[effective_destination]

                if effective_destination not in distance:
                    distance[effective_destination] = distance[idx] + 1

                if effective_destination not in visited:
                    queue.append(effective_destination)

        return distance.get(n * n, -1)


if __name__ == '__main__':
    x = Solution()
    assert x.snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]) == 4
