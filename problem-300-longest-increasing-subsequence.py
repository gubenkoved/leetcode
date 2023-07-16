from typing import List


class Solution:
    # O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i] -- max len of Longest Increasing Sequence up to i-th element # (included mandatory)
        for idx in range(1, n):
            cur = 1
            for prev_idx in range(0, idx):
                if nums[idx] > nums[prev_idx]:
                    cur = max(cur, dp[prev_idx] + 1)
            dp[idx] = cur
        return max(dp)


if __name__ == '__main__':
    x = Solution()
    print(x.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(x.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(x.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
    print(x.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
