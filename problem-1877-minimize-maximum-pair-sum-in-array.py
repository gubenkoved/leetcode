from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for idx in range(n // 2):
            res = max(res, nums[idx] + nums[n - idx - 1])
        return res
