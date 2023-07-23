from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(l, r, lean_left=True):
            if r - l <= 1:
                if lean_left:
                    if nums[l] == target:
                        return l
                    elif nums[r] == target:
                        return r
                else:
                    if nums[r] == target:
                        return r
                    elif nums[l] == target:
                        return l
                return -1

            m = (l + r) // 2

            if nums[m] >= target and lean_left or nums[m] > target:
                return binary_search(l, m, lean_left)
            else:
                return binary_search(m, r, lean_left)

        n = len(nums)

        if n == 0:
            return [-1, -1]

        left = binary_search(0, n - 1, lean_left=True)

        if left == -1:
            return [-1, -1]

        right = binary_search(0, n - 1, lean_left=False)

        return [left, right]


if __name__ == '__main__':
    x = Solution()

    print(x.searchRange([5, 7, 7, 8, 8, 10], target=8))
    print(x.searchRange([5, 6, 7, 8, 8, 10], target=7))
    print(x.searchRange([5, 6, 7, 8, 8, 10], target=9))
    print(x.searchRange([5, 5, 5, 5], target=5))
    print(x.searchRange([], target=8))
    print(x.searchRange([8], target=8))
