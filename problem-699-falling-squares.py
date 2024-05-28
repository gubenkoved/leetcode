from typing import List


class Solution:
    # the below probably only works if we add blocks in a way that
    # x coordinate is not decreasing, which is not the case
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # tracks (end_x, height) in LIFO order
        stack = []
        results = []
        cur_tallest = 0

        for start_x, length in positions:
            end_x = start_x + length
            while stack and stack[-1][0] <= start_x:
                stack.pop(-1)

            if stack:
                stack.append((end_x, stack[-1][1] + length))
            else:
                stack.append((end_x, length))

            cur_tallest = max(cur_tallest, stack[-1][1])
            results.append(cur_tallest)

        return results


if __name__ == '__main__':
    x = Solution()
    assert x.fallingSquares([[1, 2], [2, 3], [6, 1]]) == [2, 5, 5]
    assert x.fallingSquares([[6, 1], [9, 2], [2, 4]]) == [1, 2, 4]
