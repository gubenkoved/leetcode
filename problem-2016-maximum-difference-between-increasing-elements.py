from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        rolling_min = nums[0]
        for x in range(nums):
            if x <= rolling_min:
                rolling_min = x
            else:
                result = max(result, x - rolling_min)
        return result
