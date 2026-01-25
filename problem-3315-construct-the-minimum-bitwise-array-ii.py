from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # X or (X+1) basically flips FIRST zero bit from the lowest ones
        # for instance (binary):
        # 1111 OR (1111 + 1) = 1111 OR 10000 = 11111
        # 1101 OR (1101 + 1) = 1101 OR 1110 = 1111

        # now to the target number we looking for:
        # 3: 11 -> 10
        # 5: 101 -> 100
        # 7: 111 -> 11
        # 13: 1101 -> 1100

        ans = []
        for x in nums:
            cur = -1
            p = 1
            # we kind of can not "cross" the 0 as our target operation will
            # flip FIRST zero bit starting from the lowest ones
            while p & x != 0:
                cur = x - p
                p *= 2
            ans.append(cur)
        return ans
