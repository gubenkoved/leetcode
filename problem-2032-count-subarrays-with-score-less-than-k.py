from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        s, c = nums[0], 1
        n = len(nums)

        result = 0

        if s * c < k:
            result += 1

        while True:
            r += 1

            if r == n:
                break

            s += nums[r]
            c += 1

            # move l forward so that we reach the condition
            while s * c >= k and l <= r:
                l += 1
                c -= 1
                s -= nums[l - 1]

            # add all aubarrays inside [l; r] as smaller ones are all matching!
            result += r - l + 1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.countSubarrays([2,1,4,3,5], k = 10))
    print(x.countSubarrays([1,1,1], k = 5))
