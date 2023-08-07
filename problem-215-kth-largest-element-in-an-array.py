from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_select(nums, k):
            min_ = min(nums)
            max_ = max(nums)

            if k == 1:
                return max_
            elif k == len(nums):
                return min_

            if min_ == max_:
                return nums[0]

            avg = sum(nums) / len(nums)

            less = []
            bigger_or_equal = []

            for x in nums:
                if x >= avg:
                    bigger_or_equal.append(x)
                else:
                    less.append(x)

            if len(bigger_or_equal) >= k:
                return quick_select(bigger_or_equal, k)
            else:
                return quick_select(less, k - len(bigger_or_equal))

        return quick_select(nums, k)


if __name__ == '__main__':
    x = Solution()
    # print(x.findKthLargest([2, 1], 2))
    print(x.findKthLargest([3, 1, 2, 4], 2))
