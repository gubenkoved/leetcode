from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = -1
        for idx in range(0, len(nums)):
            a, b = nums[idx - 1], nums[idx]
            result = max(result, abs(a - b))
        return result
