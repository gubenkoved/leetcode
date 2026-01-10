import functools
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        @functools.lru_cache(None)
        def f(i, j):
            if i == n1 - 1:
                cur = nums1[i] * nums2[j]
                for jj in range(j, n2):
                    cur = max(cur, nums1[i] * nums2[jj])
                return cur

            if j == n2 - 1:
                cur = nums1[i] * nums2[j]
                for ii in range(i, n1):
                    cur = max(cur, nums1[ii] * nums2[j])
                return cur

            return max(
                # add (i, j) to previous max
                nums1[i] * nums2[j] + f(i + 1, j + 1),
                # take only pair (i, j) -- this is to handle previous result being negative
                nums1[i] * nums2[j],
                # skip both
                f(i + 1, j + 1),
                # skip from nums2
                f(i, j + 1),
                # skip from nums1
                f(i + 1, j),
            )

        return f(0, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.maxDotProduct([-1, -2], [3, 5]), -3)
    print(x.maxDotProduct([-1, -2], [3, 3, 5, 5]), -3)
    print(x.maxDotProduct([-5,-1,-2], [3,3,5,5]), -3)
