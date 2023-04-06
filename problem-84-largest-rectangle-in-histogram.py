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
        stack = [heights[0]]
        for idx in range(1, n):
            if heights[idx] < heights[idx - 1]:
                popped = 0
                while stack and stack[-1] > heights[idx]:
                    area = (popped + 1) * stack[-1]
                    max_area = max(max_area, area)
                    popped += 1
                    stack.pop()

                # TODO: optimize by storing width
                for _ in range(popped):
                    stack.append(heights[idx])
            stack.append(heights[idx])
        return max_area


if __name__ == '__main__':
    x = Solution()
    assert x.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert x.largestRectangleArea([2, 1, 2]) == 3
    assert x.largestRectangleArea([1] * 100000) == 100000
    assert x.largestRectangleArea([0, 9]) == 9
    assert x.largestRectangleArea([1, 2, 2]) == 4
