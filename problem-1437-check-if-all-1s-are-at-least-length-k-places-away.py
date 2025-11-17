from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -k - 1
        for idx in range(len(nums)):
            if nums[idx] == 1:
                if idx - last_one_idx <= k:
                    return False
                last_one_idx = idx
        return True
