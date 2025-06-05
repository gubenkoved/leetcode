from typing import List
import random


class Solution:
    def countSubarrays_naive(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)

        res = 0
        for l in range(n):
            for r in range(l, n):
                c = sum(1 for x in nums[l:r + 1] if x == m)
                if c >= k:
                    res += 1
        return res

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)

        l, r = 0, 0

        result = 0

        if nums[0] == m:
            counter = 1
        else:
            counter = 0

        while True:

            # slide the right pointer while we do not have k maximums
            # in the window and window is not too big
            while counter < k and r < n - 1:
                r += 1

                if nums[r] == m:
                    counter += 1

            if counter < k:
                break

            while True:
                # this windows and all the ones which are bigger to the right are matching!
                result += n - r

                # move the left pointer
                l += 1
                if nums[l - 1] == m:
                    counter -= 1
                    break

                if l >= r:
                    break

            if l >= n:
                break

        return result


def debug():
    x = Solution()

    for a_size in range(1, 10):
        for _ in range(100):
            arr = [random.randint(1, 10) for _ in range(a_size)]
            a1 = x.countSubarrays(arr, 2)
            a2 = x.countSubarrays_naive(arr, 2)
            assert a1 == a2


if __name__ == '__main__':
    # debug()

    x = Solution()
    # print(x.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
    # print(x.countSubarrays_naive(nums=[1, 3, 2, 3, 3], k=2))
    # print(x.countSubarrays(nums=[1, 4, 2, 1], k=3))
    # print(x.countSubarrays([1, 1, 100, 100, 1, 1], k=2))  # 9
    # print(x.countSubarrays([1, 1, 100, 100, 1, 1, 100], k=2))  # 13
    print(x.countSubarrays([61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], k=2))
    # print(x.countSubarrays([8, 6, 8, 8, 5], k=2))
