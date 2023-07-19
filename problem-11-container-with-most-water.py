from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        result = 0
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxArea([1,8,6,2,5,4,8,3,7]))
