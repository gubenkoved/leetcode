from typing import List
import math

# this is basically pascal triangle inspired, just count amount of
# times given number will contribute to the result
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        return sum((nums[idx] * math.comb(n - 1, idx)) % 10 for idx, num in enumerate(nums)) % 10

if __name__ == '__main__':
    x = Solution()
    print(x.triangularSum([1,2,3,4,5]))
