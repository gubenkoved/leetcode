from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 3:
            return max(nums)

        @lru_cache(maxsize=None)
        def f(left, right):
            # base cases
            if left == right:
                return nums[left]
            elif right - left == 1:
                return max(nums[left], nums[right])
            elif left > right:
                return 0

            # since all numbers are positive we either take first or second
            # from the list, since it does not make sense to skip 2 items
            # given that you could have taken 1st and get some additional
            # positive benefit
            return max(
                nums[left] + f(left + 2, right),
                nums[left + 1] + f(left + 3, right)
            )

        return max(
            nums[0] + f(2, len(nums) - 2),  # start with 0th
            nums[1] + f(3, len(nums) - 1),  # start with 1st
            nums[-1] + f(1, len(nums) - 3),  # start with last one
        )


if __name__ == '__main__':
    x = Solution()
    assert x.rob([1]) == 1
    assert x.rob([2, 3, 2]) == 3
    assert x.rob([1, 2, 3, 1]) == 4
    assert x.rob([1, 2, 3]) == 3
    assert x.rob([4, 1, 2, 7, 5, 3, 1]) == 14
    assert x.rob([2, 7, 7, 7, 4]) == 14
    assert x.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
