from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)

        # left and right are inclusive
        def search(left, right):
            if right - left <= 1:
                return right if nums[right] > nums[left] else left

            mid = (right + left) // 2

            # recursive dive
            # given that we know that mid-point is not peak (see above)
            # we then determine the slope on midpoint -- it is either
            # increasing or decreasing, and we need to choose right half if it is
            # increasing and left one otherwise
            if mid == 0 or nums[mid] > nums[mid - 1]:
                # right half
                return search(mid, right)
            else:
                return search(left, mid)

        return search(0, n - 1)


if __name__ == '__main__':
    x = Solution()


    def case(array, expected):
        actual = x.findPeakElement(array)
        assert actual in expected, 'Actual result is %s' % actual


    case([1, 2, 3, 1], [2])
    case([1, 2, 1, 3, 5, 6, 4], [1, 5])
    case([1, 2], [1])
    case([1], [0])
