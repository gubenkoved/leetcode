# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with
# a number on it represented by an array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
# If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a
# balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
# Constraints:
# * n == nums.length
# * 1 <= n <= 300
# * 0 <= nums[i] <= 100

from typing import List, Tuple
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def maxCoins_bruteForce(self, nums: Tuple[int]) -> int:
        # print(f'{nums}')

        n = len(nums)

        # end condition
        if n == 1:
            # print(f'{nums} -> {nums[0]}')
            return nums[0]

        best = 0
        for burst_at in range(0, n):
            score = (nums[burst_at]
                     * (nums[burst_at - 1] if burst_at - 1 >= 0 else 1)
                     * (nums[burst_at + 1] if burst_at + 1 < n else 1))
            nums2 = tuple(nums[:burst_at] + nums[burst_at+1:])
            best2 = self.maxCoins_bruteForce(nums2)
            best = max(best, score + best2)

        # print(f'{nums} -> BEST {best}')
        return best

    # did not solve myself
    def maxCoins(self, nums: List[int]) -> int:
        # see here:
        # https://leetcode.com/problems/burst-balloons/discuss/892552/For-those-who-are-not-able-to-understand-any-solution-WITH-DIAGRAM

        # solve(i, j) gives best score to get when bursting [i, i+1, ..., j] balloons
        @lru_cache(None)
        def solve(i, j) -> int:
            # the stop conditions
            if i > j:
                return 0

            if i == j:
                return (
                    nums[i]
                    * (nums[i - 1] if i - 1 >= 0 else 1)
                    * (nums[i + 1] if i + 1 < len(nums) else 1)
                )

            # solve subproblems under assumption that k-th balloon is burst as LAST one
            # then the subproblems are independent
            best = 0
            for k in range(i, j + 1):
                left_result = solve(i, k - 1)
                right_result = solve(k + 1, j)
                this_result = (
                    nums[k]
                    * (nums[i - 1] if i - 1 >= 0 else 1)
                    * (nums[j + 1] if j + 1 < len(nums) else 1)
                )
                best = max(best, left_result + right_result + this_result)

            # print(f'{nums[i:j+1]} -> {best}')
            return best

        return solve(0, len(nums) - 1)


if __name__ == '__main__':
    x = Solution()
    assert x.maxCoins([3, 1, 5, 8]) == 167
    assert x.maxCoins([1] * 10) == 10
    assert x.maxCoins([7, 9, 8, 0, 7, 1, 3, 5, 5, 2]) == 1582
    assert x.maxCoins([8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]) == 3394
    assert x.maxCoins([18,2,8,47,99,80,12,75,97,3,46,75,71,99,55,54,39,55,73,21,67,35,89,60,95,45,89,96,61,70,30,34,80,7,42,10,8,72,9,84,9,49,11,47,87,84,76,87,40,98,25,10,6,13,94,43,34,72,79,52,75,91,45,45,90,36,9,61,58,80,13,18,67,17,4,92,71,7,44,72,45,41,72,72,94,20,21,42,15,45,35,5,6,25,17,87,98,75,27,74,11,48,87,50,58,9,36,90,33,35,94,72,84,1,21,4,75,80,28,48,57,40,87,69,89,93,28,100,44,52,87,17,15,65,67,72,5,92,43,90,99,53,99,55,44,22,78,93,30,72,0,28,42,83,99,1,75,2,61,1,25,73,78,86,20,75,15,53,44,51,9,3,85,56,83,22,18,5,73,10,53,56,29,87,76,74,12,83,33,68,20,51,69,31,92,24,25,51,94,26,34,25,4,56,19,56,0,58,22,94,53,78,38,20,29,74,46,21,44,16,77,3,49,79,28,83,61,13,39,12,91,50,60,92,100,2,5,52,98,3,80,11,34,60,35,1,30,91,51,52,39,72,4,29,86,64,39,51,74,99,99,32,12,16,61,88,5,82,85,19,45,80,45,5,63,23,51,91,97,24,35,42,60,100,8,31,39,54,80,66,28,52,75,25,66,51,20,98,99,78]) == 111830214
