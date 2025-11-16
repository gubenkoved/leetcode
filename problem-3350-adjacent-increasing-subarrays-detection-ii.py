from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        nums.append(float('-inf'))

        n = len(nums)
        inc_len = [1] * n

        result = 1
        max_len = 1
        prev_len = 1
        for idx in range(1, n):
            if nums[idx] > nums[idx - 1]:
                inc_len[idx] = inc_len[idx - 1] + 1
            else:  # new subsequence
                inc_len[idx] = 1
                result = max(result, min(inc_len[idx - 1], prev_len))
                prev_len = inc_len[idx - 1]
                max_len = max(max_len, prev_len)

        # we can also split one single big increasing subsequence in two
        result = max(result, max_len // 2)

        return result