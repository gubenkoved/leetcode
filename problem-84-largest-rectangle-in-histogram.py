from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0

        for idx in range(n):
            # check how much to the right we can go
            start_idx = idx
            end_idx = idx

            while end_idx < n - 1 and heights[end_idx + 1] >= heights[idx]:
                end_idx += 1

            while start_idx > 0 and heights[start_idx - 1] >= heights[idx]:
                start_idx -= 1

            max_area = max(max_area, (end_idx - start_idx + 1) * heights[idx])

        # print(max_area)
        return max_area


if __name__ == '__main__':
    x = Solution()
    assert x.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert x.largestRectangleArea([2, 1, 2]) == 3
    assert x.largestRectangleArea([1] * 100000) == 100000
