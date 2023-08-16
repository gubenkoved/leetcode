from typing import List
from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left_prefix_sums = {}
        n = len(nums)

        rolling_sum = 0
        for right in range(n):
            rolling_sum += nums[right]

            if rolling_sum not in left_prefix_sums:
                left_prefix_sums[rolling_sum] = deque()

            left_prefix_sums[rolling_sum].append(right)

        count = 0

        # now check all ranges moving left edge forward
        # note: left is inclusive
        rolling_sum = 0
        for left in range(n):
            matching_bucket = left_prefix_sums.get(k + rolling_sum)

            if matching_bucket:
                # remove ones where right edge is to the left of the
                while matching_bucket and matching_bucket[0] < left:
                    matching_bucket.popleft()
                count += len(matching_bucket)

            rolling_sum += nums[left]

        return count


if __name__ == '__main__':
    x = Solution()
    # print(x.subarraySum([1, 1, 1], k=2))
    # print(x.subarraySum([1, 2, 3], k=3))
    print(x.subarraySum([-1, -1, 1], k=0))
