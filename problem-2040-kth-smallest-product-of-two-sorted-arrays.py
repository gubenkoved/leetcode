import bisect
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs_less_than_threshold(arr, el, threshold):
            if el > 0:
                return bisect.bisect_right(arr, threshold // el)
            elif el < 0:
                return len(arr) - bisect.bisect_left(arr, -(-threshold // el))
            else:
                assert el == 0
                if threshold < 0:
                    return 0
                else:
                    return len(arr)

        special1 = [nums1[0], nums1[-1]]
        special2 = [nums2[0], nums2[-1]]

        l = min(x * y for x in special1 for y in special2)
        r = max(x * y for x in special1 for y in special2)

        while l <= r:
            count = 0
            m = (l + r) // 2
            for x in nums1:
                count += count_pairs_less_than_threshold(nums2, x, m)
            if count < k:
                l = m + 1
            else:
                r = m - 1

        return l


if __name__ == '__main__':
    x = Solution()
    # print(x.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))
    # print(x.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
    # print(x.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))
    # print(x.kthSmallestProduct(nums1=[3], nums2=[2], k=1))
    # print(x.kthSmallestProduct([-8,-8,3,7], [-1], 3))
    # print(x.kthSmallestProduct([-6,-5,1], [-8,-5,-5,-5,-4,-3,0,9], 4))
    # print('expected 32', x.kthSmallestProduct([-10,-9,-8,-5,-3,-2,1,2,4,8], [-9,-8,-8,-4,-4,-3,-1,0,4], 73))
    print(x.kthSmallestProduct([-2,-1,0,1,2], [-3,-1,2,4,5], 3))
