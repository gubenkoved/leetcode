from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def find(l_incl, r_excl):
            if r_excl - l_incl <= 1:
                if nums[l_incl] >= target:
                    return l_incl
                else:
                    return r_excl

            mid = (l_incl + r_excl) // 2

            if nums[mid] >= target:
                return find(l_incl, mid)
            else:
                return find(mid, r_excl)

        return find(0, len(nums))


if __name__ == '__main__':
    x = Solution()
    print(x.searchInsert([1, 3, 5, 6], target=5))
    print(x.searchInsert([1, 3, 5, 6], target=2))
    print(x.searchInsert([1, 3, 5, 6], target=7))
    print(x.searchInsert([1, 3, 5, 6], target=0))
