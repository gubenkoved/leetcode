import collections
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = collections.defaultdict(lambda: 0)
        for x in nums:
            freq[x] += 1

        for x, f in freq.items():
            if f == len(nums) // 2:
                return x

        return -1
