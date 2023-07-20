from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_right = [0] * n

        max_right[n - 1] = height[n - 1]
        for idx in range(n - 2, -1, -1):
            max_right[idx] = max(max_right[idx + 1], height[idx])

        trapped = 0
        max_left = height[0]
        for idx in range(1, n - 1):
            max_level = min(max_left, max_right[idx + 1])
            trapped += max(0, max_level - height[idx])
            max_left = max(max_left, height[idx])
        return trapped


if __name__ == '__main__':
    x = Solution()
    print(x.trap([0,1,0,2,1,0,1,3,2,1,2,1]))