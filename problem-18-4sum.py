from typing import List
import bisect


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        result = []
        taken = [None] * 4
        nums = sorted(nums)

        def f(idx, n, leftover):
            if leftover < n * nums[idx]:
                return

            if n == 1:
                found_idx = bisect.bisect_left(nums, leftover, lo=idx)

                if found_idx != l and nums[found_idx] == leftover:
                    taken[0] = nums[found_idx]
                    result.append(list(taken))
                return

            i = idx
            while i < l - n + 1:
                taken[n - 1] = nums[i]
                f(i + 1, n - 1, leftover - nums[i])
                i += 1
                while i < l - n + 1 and nums[i] == nums[i - 1]:
                    i += 1

        f(0, 4, target)

        print('RESULT: %s' % result)

        return result


if __name__ == '__main__':
    x = Solution()
    x.fourSum([1, 0, -1, 0, -2, 2], target=0)
    x.fourSum([2, 2, 2, 2, 2], target=8)
    x.fourSum(
        [-483, -464, -417, -372, -315, -303, -283, -282, -267, -265, -262, -256, -254, -248, -247, -245, -200, -200,
         -194, -192, -183, -155, -83, -69, -59, -44, -42, -40, -24, -18, -14, -11, 0, 4, 10, 28, 38, 59, 87, 126, 135,
         147, 151, 152, 162, 187, 211, 214, 218, 248, 274, 282, 287, 288, 329, 331, 338, 364, 366, 384, 405, 476, 477,
         488], 1563)
