from typing import List


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_n(nums: List[int]) -> int:
    if len(nums) == 2:
        return gcd(nums[0], nums[1])
    return gcd(nums[0], gcd_n(nums[1:]))


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        m = None

        # finding the smallest subarray which would give 1 GCD (O(n^2))
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if gcd_n(nums[i:j+1]) == 1:
                    if m is None or j - i < m:
                        m = j - i

        if m is None:
            return -1

        # on the calculation:
        # m is really subarray size (let's denote as M) minus one
        # when subarray has GCD it means that if we handle its M-1 (or m) pairs
        # we will end up with at least one "1", which would leave us to just step
        # by step turn any neighbor to one (there will be N minus 1) these
        # where N is amount of non-1 numbers;
        # if fact if there is at least one "1" we can skip gcd subarray
        # altogether and just count amount of non "1"

        return sum(1 for x in nums if x != 1) + m - 1


if __name__ == '__main__':
    x = Solution()
    print(x.minOperations([6, 10, 15]), 4)  # [2 * 3, 2 * 5, 3 * 5]
    print(x.minOperations([6, 10, 15, 30]), 5)  # [2 * 3, 2 * 5, 3 * 5, 2 * 3 * 5]