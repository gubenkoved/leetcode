from typing import List
import bisect


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.kthSmallestProduct_naive(nums1, nums2, k)

        # split nums2 into two collections to avoid negative numbers
        for idx in range(len(nums2)):
            if nums2[idx] >= 0:
                nums2_1 = nums2[idx:]  # positive from the start
                nums2_2 = nums2[:idx]  # negative from the start
                break
        else:
            # all negative
            nums2_1 = []
            nums2_2 = nums2


        # invert the nums2_2 or reverse the order to get it sorted
        nums2_2_inv = [-x for x in reversed(nums2_2)]

        # nums2_1 is paired to the nums1, and nums2_2 is paired against
        # numbers multiplied by -1 to compensate;

        # then this task is unified as we have two positive arrays from one side
        # and we will need to count in them both when we binary search the answer;

        nums1_inv = [-x for x in reversed(nums1)]

        # returns count of pairs which are below the threshold inside the a, b
        # lists; lists are assumed sorted and b does NOT have negative numbers
        # so that implementation is free of edge cases
        def count_pairs_less_or_equal(a, b, threshold):
            res = 0
            max_product = None
            for x in b:
                # find index in a where numbers multiplied by x will be less than
                # threshold
                if x != 0:
                    y = threshold / x
                    a_idx = bisect.bisect_right(a, y)
                    res += a_idx
                else:  # x == 0
                    a_idx = bisect.bisect_right(a, 0)
                    if threshold < 0:
                        # we can not get product less than or equal to 0 if
                        # one of the multipliers is 0, because product is 0 too
                        # which is more than threshold
                        continue
                    elif threshold == 0:
                        # all the items in the "a" work as both threshold and
                        # b's element are 0
                        res += len(a)
                        a_idx = len(a)
                    else:
                        assert threshold > 0
                        res += a_idx

                if a_idx != 0:
                    pr = a[a_idx - 1] * x
                    if max_product is None or pr > max_product:
                        max_product = pr
            assert max_product is None or max_product <= threshold
            return res, max_product

        special1 = [nums1[0], nums1[-1]]
        special2 = [nums2[0], nums2[-1]]

        l = min(x * y for x in special1 for y in special2)
        r = max(x * y for x in special1 for y in special2)

        # solution is in (l; r]
        while l < r:
            m = l + (r - l) // 2

            # edge case
            if m == l:
                m += 1

            # print('check %s' % m)
            cnt1, _ = count_pairs_less_or_equal(nums1, nums2_1, m)
            cnt2, _ = count_pairs_less_or_equal(nums1_inv, nums2_2_inv, m)
            cnt = cnt1 + cnt2

            if cnt < k:
                l = m
            elif cnt > k:
                r = m
            else:
                r = m
                break

            if l == r - 1:
                break

        print(f'{r=}')

        _, mp1 = count_pairs_less_or_equal(nums1, nums2_1, r)
        _, mp2 = count_pairs_less_or_equal(nums1_inv, nums2_2_inv, r)

        if mp1 is not None and mp2 is not None:
            mp = max(mp1, mp2)
        elif mp1 is not None:
            mp = mp1
        elif mp2 is not None:
            mp = mp2
        else:
            assert False, 'what'

        return mp

    def kthSmallestProduct_naive(self, nums1: List[int], nums2: List[int], k: int) -> int:
        products = sorted([x * y for x in nums1 for y in nums2])
        print(products[k - 1], products)
        return products[k - 1]



if __name__ == '__main__':
    x = Solution()
    # print(x.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))
    # print(x.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
    # print(x.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))
    # print(x.kthSmallestProduct(nums1=[3], nums2=[2], k=1))
    # print(x.kthSmallestProduct([-8,-8,3,7], [-1], 3))
    # print(x.kthSmallestProduct([-6,-5,1], [-8,-5,-5,-5,-4,-3,0,9], 4))
    print('expected 32', x.kthSmallestProduct([-10,-9,-8,-5,-3,-2,1,2,4,8], [-9,-8,-8,-4,-4,-3,-1,0,4], 73))
