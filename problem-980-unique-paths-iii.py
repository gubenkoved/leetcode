from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        counter = 0
        path_len = 0

        start = None
        finish = None

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != -1:
                    path_len += 1

                if grid[row][col] == 1:
                    start = (row, col)
                elif grid[row][col] == 2:
                    finish = (row, col)

        assert start is not None
        assert finish is not None

        current_path_set = {start}

        def walk(row, col):
            nonlocal counter

            if (row, col) == finish and len(current_path_set) == path_len:
                # found path!
                counter += 1

            candidates = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]

            for candidate in candidates:
                if candidate[0] < 0 or candidate[0] >= rows:
                    continue
                if candidate[1] < 0 or candidate[1] >= cols:
                    continue

                if candidate in current_path_set:
                    continue

                if grid[candidate[0]][candidate[1]] == -1:
                    continue

                current_path_set.add(candidate)
                walk(candidate[0], candidate[1])
                current_path_set.discard(candidate)

        walk(start[0], start[1])

        return counter


if __name__ == '__main__':
    x = Solution()
    print(x.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
