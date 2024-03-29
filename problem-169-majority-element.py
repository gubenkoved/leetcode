from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    x = Solution()
    print(x.majorityElement([3, 2, 3]))
    print(x.majorityElement([2, 2, 1, 1, 1, 2, 2]))
