from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        def find(left, right):
            if right - left <= 1:
                return min(nums[left], nums[right])

            mid = (left + right) // 2

            if nums[mid] < nums[left]:
                return find(left, mid)
            else:
                return find(mid, right)

        return find(0, len(nums) - 1)


if __name__ == '__main__':
    x = Solution()
    print(x.findMin([11,13,15,17]))