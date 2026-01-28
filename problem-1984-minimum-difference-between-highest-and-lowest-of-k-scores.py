from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = float('+inf')
        nums.sort()
        for idx in range(k - 1, n):
            delta = nums[idx] - nums[idx - k + 1]
            result = min(result, delta)
        return result
