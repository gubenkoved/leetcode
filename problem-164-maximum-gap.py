# Given an integer array nums, return the maximum difference between two successive
# elements in its sorted form. If the array contains less than two elements, return 0.
#
# You must write an algorithm that runs in linear time and uses linear extra space.
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9

from typing import List
from collections import defaultdict


# did NOT solve it myself
class Solution:
    # O(n logn)
    def maximumGap_slow(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        max_diff = float('-inf')
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx - 1] > max_diff:
                max_diff = nums[idx] - nums[idx - 1]
        return max_diff

    # O(C), where C is a huge constant...
    def maximumGap_v1(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        m = max(nums)
        counts = [0] * (m + 1)

        for x in nums:
            counts[x] += 1

        max_gap = float('-inf')
        prev = None

        for idx in range(0, m + 1):
            if counts[idx] > 0:
                if prev is not None:
                    max_gap = max(max_gap, idx - prev)
                prev = idx

        return max_gap

    def maximumGap(self, nums: List[int]) -> int:
        # distribute numbers into (n-1) buckets that cover the range of number fully
        # the maximum gap will be no smaller than ceiling [(high - low ) / (n - 1)].
        # bucket size is chosen so that max gap can not be in the same bucket, and we would
        # need (n - 1) buckets for that
        high, low, n = max(nums), min(nums), len(nums)

        if n < 2:
            return 0
        elif n == 2:
            return high - low

        buckets = defaultdict(list)
        for num in nums:
            bucket_idx = n - 2 if num == high else (num - low) * (n - 1) // (high - low)
            buckets[bucket_idx].append(num)

        non_empty_buckets = []

        for bucket_idx in range(0, n - 1):
            if buckets.get(bucket_idx):
                non_empty_buckets.append(buckets[bucket_idx])

        if len(non_empty_buckets) == 1:
            return max(non_empty_buckets[0]) - min(non_empty_buckets[0])

        # now find the max gap using the fact that it can not be inside the bucket
        # it has to be on the edge between the buckets because max diff between numbers
        # in the bucket is ceiling((high - low) // (n - 1))
        max_gap = float('-inf')

        for idx in range(1, len(non_empty_buckets)):
            b1 = non_empty_buckets[idx - 1]
            b2 = non_empty_buckets[idx]
            max_gap = max(max_gap, min(b2) - max(b1))

        return max_gap


if __name__ == '__main__':
    x = Solution()

    # The sorted form of the array is [1, 3, 6, 9], either (3, 6) or (6, 9) has the maximum difference 3
    # assert x.maximumGap([3, 6, 9, 1]) == 3
    # assert x.maximumGap([9, 3, 1, 6]) == 3
    # assert x.maximumGap([9, 6, 3, 1]) == 3
    #
    # assert x.maximumGap([1, 2, 3, 4, 5, 6]) == 1
    # assert x.maximumGap([1, 3, 5, 2, 4, 6]) == 1
    # assert x.maximumGap([1, 6, 2, 4, 3, 5]) == 1
    #
    # assert x.maximumGap([1, 2, 3, 8, 9]) == 5
    # assert x.maximumGap([1, 9, 2, 8, 3]) == 5
    # assert x.maximumGap([8, 9, 2, 1, 3]) == 5
    #
    # assert x.maximumGap([1, 10000000]) == (10000000 - 1)
    #
    # assert x.maximumGap([2, 99999999]) == (99999999 - 2)
    # assert x.maximumGap([1, 1, 1, 1]) == 0
