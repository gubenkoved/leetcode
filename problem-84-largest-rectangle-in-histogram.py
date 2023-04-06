from typing import List


class SlowSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0
        max_area_info = (0, 0, 0)

        for idx in range(n):

            if heights[idx] <= max_area_info[2] and max_area_info[0] <= idx <= max_area_info[1]:
                continue

            # check how much to the right we can go
            start_idx = idx
            end_idx = idx

            while end_idx < n - 1 and heights[end_idx + 1] >= heights[idx]:
                end_idx += 1

            while start_idx > 0 and heights[start_idx - 1] >= heights[idx]:
                start_idx -= 1

            area = (end_idx - start_idx + 1) * heights[idx]

            if area > max_area:
                max_area = area
                max_area_info = (start_idx, end_idx, heights[idx])

        print(max_area)
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        max_area = 0
        stack = [(heights[0], 1)]  # (height, width) tuples
        for idx in range(1, n):
            popped_width = 0
            if heights[idx] < heights[idx - 1]:
                while stack and stack[-1][0] > heights[idx]:
                    h, w = stack.pop()
                    area = (popped_width + w) * h
                    max_area = max(max_area, area)
                    popped_width += w
            stack.append((heights[idx], 1 + popped_width))
        return max_area


if __name__ == '__main__':
    x = Solution()
    assert x.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert x.largestRectangleArea([2, 1, 2]) == 3
    assert x.largestRectangleArea([1] * 100000) == 100000
    assert x.largestRectangleArea([0, 9]) == 9
    assert x.largestRectangleArea([1, 2, 2]) == 4
