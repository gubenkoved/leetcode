import math
import time
from typing import List

STARTED_AT = time.time()
PRINT_ORIG = print


def print(text):
    PRINT_ORIG('[%6.3f] %s' % (time.time() - STARTED_AT, text))


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        print('solving for %s...' % nums)

        m = min(nums)
        nums = [x - m for x in nums]

        # try to optimize traversal order...
        nums = sorted(nums)
        nums2 = nums[::2] + nums[1::2]
        nums = nums2

        k = len(nums)
        s = sum(nums)

        ideal = s % 2
        min_difference = math.inf
        counter = 0

        def pick(n, idx, cur_sum):
            nonlocal min_difference
            nonlocal counter

            # print('  %spick(%s, %s, %s)' % ('   ' * (k//2 - n) * 2, n, idx, cur_sum))

            counter += 1

            if n == 0:
                cur_difference = abs(s - 2 * cur_sum)
                if cur_difference < min_difference:
                    print('  found %d' % cur_difference)
                    min_difference = cur_difference
                return

            # cut if no better is possible
            if min_difference == ideal:
                return

            if cur_sum > s // 2:
                return

            for i in range(idx, k):
                # filter out cases where we know there will be not enough numbers
                # even if we take all of the leftover ones to the right
                if n <= k - i:
                    pick(n - 1, i + 1, cur_sum + nums[i])

        pick(k // 2, 0, 0)

        print('checked %d combinations' % counter)

        return min_difference


if __name__ == '__main__':
    x = Solution()

    print(x.minimumDifference([3, 9, 7, 3]))
    print(x.minimumDifference([-36, 36]))
    print(x.minimumDifference([2, -1, 0, 4, -2, -9]))
    print(x.minimumDifference([1, 10]))
    print(x.minimumDifference([4, 4, 4, 10]))
    print(x.minimumDifference([1] * 5 + [10]))
    # print(x.minimumDifference([100] * 29 + [200]))
    print(x.minimumDifference(
        [7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283, 5919119,
         3093450, 1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873, 302974, 7656726,
         -2572679, 0, 2121026, -5743797, -8897395, -9699694]))
    print(x.minimumDifference(
        [-7016943, 0, 2205243, -794066, -6795006, 5322408, 9699476, 6544247, 6992622, 7272161, 5469637, 4806999,
         -8562708, -5242263, 9037593, -2746735, 8072395, -1386148, 4745179, 3801334, -4086041, 0, 555427, -9249908,
         5045948, -7943170, 1665466, 9514306, 7960606, -142676]))
    print(x.minimumDifference(
        [-9812803, -9143114, -2074989, -5685138, -7352242, 3440344, -2609145, -8086215, -8560628, 1649530, 9514043,
         -6703707, 2999701, 4558830, -92232, -7002104, -563926, 5824475, 9273165, -5659380, -985282, 5974935, 5385506,
         9920972, 1291494, -3581309, -4123458, -1468372, 2224246, 7135705]
    ))
