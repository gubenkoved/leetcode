from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # check if possible to have triangle
        nums.sort()

        if nums[2] >= nums[0] + nums[1]:
            return 'none'

        unique_count = len(set(nums))
        if unique_count == 1:
            return 'equilateral'
        elif unique_count == 2:
            return 'isosceles'
        else:
            return 'scalene'
