from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = nums[0]
        max_ = nums[0]
        result = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] >= 0:
                min_, max_ = min_ * nums[idx], max_ * nums[idx]
            elif nums[idx] < 0:
                min_, max_ = max_ * nums[idx], min_ * nums[idx]

            min_ = min(min_, nums[idx])
            max_ = max(max_, nums[idx])

            # update the max
            result = max(result, max_)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxProduct([2, 3, -2, 4]))
    print(x.maxProduct([-2]))
    print(x.maxProduct([-2, 3]))
    print(x.maxProduct([-2, 3, 4]))
    print(x.maxProduct([-2, 3, -4]))
    print(x.maxProduct([2, -5, -2, -4, 3]))
