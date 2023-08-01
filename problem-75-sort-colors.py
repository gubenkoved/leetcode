from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        for x in nums:
            counts[x] += 1

        ptr = 0

        for color in range(3):
            for _ in range(counts[color]):
                nums[ptr] = color
                ptr += 1
