from typing import List
from math import ceil


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # stage 1 -- find the rotation offset -- index at while we drop in value
        # stage 2 -- regular binary search over virtual array given we know the offset

        def find_offset(l, r):
            if r - l == 1:
                return r
            m = ceil((l + r) / 2.0)
            if nums[l] < nums[m]:
                return find_offset(m, r)
            else:
                return find_offset(l, m)
            pass

        offset = find_offset(0, len(nums) - 1) if nums[0] > nums[-1] else 0

        # print('offset %s' % offset)

        n = len(nums)

        def real_idx(idx):
            return (idx + offset) % n

        def val(idx):
            return nums[real_idx(idx)]

        def binary_find(l, r):
            if r - l <= 1:
                if val(l) == target:
                    return real_idx(l)
                elif val(r) == target:
                    return real_idx(r)
                else:
                    return -1
            m = (l + r) // 2

            if val(m) < target:
                return binary_find(m, r)
            else:
                return binary_find(l, m)

        return binary_find(0, len(nums) - 1)


if __name__ == '__main__':
    x = Solution()
    print(x.search([1, 2, 3, 4, 5, 6], 5))
    print(x.search([4, 5, 6, 1, 2, 3], 5))
    print(x.search([6, 1, 2, 3, 4, 5], 5))
