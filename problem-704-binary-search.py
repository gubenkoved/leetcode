from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find(left_incl, right_excl):
            if right_excl - left_incl <= 1:
                if nums[left_incl] == target:
                    return left_incl
                else:
                    return -1

            mid = (right_excl + left_incl) // 2

            if nums[mid] > target:
                return find(left_incl, mid)
            elif nums[mid] < target:
                return find(mid, right_excl)
            else:
                return mid

        return find(0, len(nums))
