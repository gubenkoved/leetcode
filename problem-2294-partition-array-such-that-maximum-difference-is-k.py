from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()

        start = 0
        end = 0

        n = len(nums)

        while start < len(nums):
            while end < n - 1 and nums[end + 1] - nums[start] <= k:
                end += 1

            start = end + 1
            end = start

            result += 1

        return result
