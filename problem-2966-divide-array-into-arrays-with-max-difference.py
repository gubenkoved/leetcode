from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for idx in range(0, n - 3 + 1, 3):
            group = nums[idx:idx + 3]
            if group[-1] - group[0] > k:
                return []
            result.append(group)
        return result
