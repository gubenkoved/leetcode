from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = abs(nums[-1] - nums[0])
        for a, b in zip(nums, nums[1:]):
            result = max(result, abs(a - b))
        return result
