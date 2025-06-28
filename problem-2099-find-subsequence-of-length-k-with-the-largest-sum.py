from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [
            t[1] for t in sorted(
                sorted(
                    enumerate(nums), key=lambda t: t[1]
                )[-k:],
                key=lambda t: t[0]
            )
        ]
