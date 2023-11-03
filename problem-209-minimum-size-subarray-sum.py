from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left and right pointers
        l, r = 0, 0

        # sum between l and r pointers inclusive both ends
        s = nums[0]

        # best size -- solution to the problem
        best = 0

        # edge case -- we already have a solution with 1 sized range
        if s >= target:
            return 1

        while r != len(nums) - 1:
            # phase 1: try to exceed target sum
            while s < target and r < len(nums) - 1:
                r += 1
                s += nums[r]

            # phase 2: try to optimize the range size to the minimum
            while s - nums[l] >= target:
                s -= nums[l]
                l += 1

            # note we should handle the case where we do not have enough sum still
            if s >= target:
                if best == 0 or r - l + 1 < best:
                    best = r - l + 1

            # advance left pointer
            s -= nums[l]
            l += 1

        return best


if __name__ == '__main__':
    x = Solution()
    assert x.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert x.minSubArrayLen(target=4, nums=[1, 4, 4]) == 1
    assert x.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
