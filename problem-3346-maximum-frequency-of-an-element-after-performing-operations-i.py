from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_num = max(nums)
        freqs = [0] * (max_num + 1)

        for x in nums:
            freqs[x] += 1

        # now for each x we can count how many we can get in the radius of k
        freqs_prefix_sums = [0] * (max_num + 1)

        for idx in range(len(freqs)):
            freqs_prefix_sums[idx] = freqs[idx]
            if idx > 0:
                freqs_prefix_sums[idx] += freqs_prefix_sums[idx - 1]

        def prefix_sum_at(idx):
            if idx >= len(freqs_prefix_sums):
                return freqs_prefix_sums[len(freqs_prefix_sums) - 1]

            if idx < 0:
                return 0

            return freqs_prefix_sums[idx]

        def range_sum(a_incl, b_incl) -> int:
            return prefix_sum_at(b_incl) - prefix_sum_at(a_incl - 1)

        result = 0
        # suppose "x" would have max frequency
        for x in range(max_num + 1):
            # left radius is [x - k, x)
            # right radius is (x, x + k)
            # which we can calc the sum for in O(1) using prefix sums
            cur = freqs[x] + min(
                numOperations,
                range_sum(x - k, x - 1) + range_sum(x + 1, x + k))
            result = max(result, cur)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2), 2)
