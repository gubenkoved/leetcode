from typing import List
import math


class Solution:
    # O(n)
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        reminder = total_sum % p

        if reminder == 0:
            return 0

        n = len(nums)

        # in other words what we are looking is subarray which
        # sum mod p is exactly equal to "reminder" so that we can subtract it
        # from the whole array and get what is left divisible by p without
        # any reminder

        # intuitively obvious:
        # (a - b) mod x = (a mod x) - (b mod x) mod x
        # see https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-addition-and-subtraction

        result = math.inf
        cur_sum = 0
        prefix_sum_reminder_to_rightmost_idx_map = {}

        # handles edge case for whole prefix being dropped
        prefix_sum_reminder_to_rightmost_idx_map[0] = -1

        for idx in range(n):
            cur_sum += nums[idx]
            cur_sum_reminder = cur_sum % p

            # what we are looking here is another prefix sum PS2
            # so that (PS - PS2) mod p = r, which would mean there is a
            # subarray which has a sum reminder equal to "r" and if we drop it
            # then leftover array will have reminder 0 (so fully divisible by p)

            # in other words we want
            # (PS mod p) - (PS2 mod p) mod p = r
            # ^^^^^^^^^^               ^^^^^^^^^
            #   known                    known

            # (PS2 mod p) is either:
            # 0 + r - (PS mod p)    if (PS mod p) <= r
            # p + r - (PS mod p)    otherwise

            # if cur_sum_reminder >= reminder:
            #     target_reminder = cur_sum_reminder - reminder
            # else:
            #     target_reminder = p + (cur_sum_reminder - reminder)
            target_reminder = (p + (cur_sum_reminder - reminder)) % p

            if target_reminder in prefix_sum_reminder_to_rightmost_idx_map:
                result = min(result, idx - prefix_sum_reminder_to_rightmost_idx_map[target_reminder])

            prefix_sum_reminder_to_rightmost_idx_map[cur_sum_reminder] = idx

        if result == math.inf:
            return -1

        if result == n:
            return -1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minSubarray([1, 2, 3, 13], 13))
    print(x.minSubarray([3, 1, 4, 2], 6))
    print(x.minSubarray([6, 3, 5, 2], 9))
    print(x.minSubarray([1, 2, 3], 3))
