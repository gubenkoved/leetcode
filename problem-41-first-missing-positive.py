from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for idx, x in enumerate(nums):
            if 0 >= x or x > n:
                nums[idx] = n + 1

        for idx, x in enumerate(nums):
            if abs(x) == n + 1:
                continue
            val = abs(x)
            # remember that we saw the "val"
            nums[val - 1] = -abs(nums[val - 1])

        # print(nums)

        for num in range(n):
            if nums[num] >= 0:
                return num + 1
        return n + 1


if __name__ == '__main__':
    # x = Solution()
    # print(x.firstMissingPositive([0, 1, 2]))
    pass