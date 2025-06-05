from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0
        for idx in range(len(nums) - 2):
            a, b, c = nums[idx:idx + 3]
            if 2 * (a + c) == b:
                result += 1
        return result
