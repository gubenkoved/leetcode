from typing import List
import bisect


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if nums[i] > target:
                continue
            # find j which contains sum for nums[i], nums[j] <= target
            j = bisect.bisect_right(nums, target - nums[i])
            if j == i and nums[i] + nums[j] <= target:
                result += 1
            elif j > i:
                result += 2 ** (j - i - 1)
        return result % (10**9 + 7)



if __name__ == '__main__':
    x = Solution()
    print(x.numSubseq([3, 5, 6, 7], target=9))
    print(x.numSubseq([3, 3, 6, 8], target=10))
    print(x.numSubseq([2, 3, 3, 4, 6, 7], target=12))
