from typing import List
import bisect


class Solution:
    # O(n^2)
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i] -- max len of Longest Increasing Sequence up to i-th element # (included mandatory)
        for idx in range(1, n):
            cur = 1
            for prev_idx in range(0, idx):
                if nums[idx] > nums[prev_idx]:
                    cur = max(cur, dp[prev_idx] + 1)
            dp[idx] = cur
        return max(dp)

    # O(n * logn)
    def lengthOfLIS_smartass(self, nums: List[int]) -> int:
        # I've looked up this approach, it would be very very hard to come up
        # with such algorithm from scratch...

        # tails is an array where tail[L] denotes minimal value that terminates
        # LIS of len L (meaning tail[1] is a minimal value, tail[2] is minimal value
        # that terminates LIST of len 2);
        # such array can be maintained for log n on each step because tails as it
        # might be obvious now is increasing sequence;
        # in order to maintain it on each new value we will need to find rightmost
        # bucket where value is less than tail[L], if no such bucket exists
        # new has to be created; finding the bucket is possible with binary search
        # in log time
        tails = [float('-inf')]

        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails) - 1

    # lengthOfLIS = lengthOfLIS_dp
    lengthOfLIS = lengthOfLIS_smartass


if __name__ == '__main__':
    x = Solution()
    print(x.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(x.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(x.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
    print(x.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
