from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        nums.append(float('-inf'))
        n = len(nums)
        prev_inc_subarray_len = 1
        cur_inc_subarray_len = 1
        max_inc_subarray_len = 1
        for idx in range(1, n):
            if nums[idx] > nums[idx - 1]:
                cur_inc_subarray_len += 1
            else:
                if cur_inc_subarray_len >= k and prev_inc_subarray_len >= k:
                    return True
                prev_inc_subarray_len = cur_inc_subarray_len
                max_inc_subarray_len = max(max_inc_subarray_len, cur_inc_subarray_len)
                cur_inc_subarray_len = 1
        return max_inc_subarray_len >= k * 2
