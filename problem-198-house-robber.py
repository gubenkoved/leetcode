from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache()
        def solve(start_idx):
            if start_idx >= n:
                return 0

            # we either take 0-th element or 1-st element (starting at start point)
            return max(
                nums[start_idx] + solve(start_idx + 2),
                nums[start_idx + 1] + solve(start_idx + 3) if start_idx + 1 <= n - 1 else 0,
            )

        return solve(0)


if __name__ == '__main__':
    x = Solution()
    print(x.rob([1, 2, 3, 1]))
    print(x.rob([2, 7, 9, 3, 1]))
