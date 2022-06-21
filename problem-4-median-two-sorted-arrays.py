from typing import List


# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).


def median(a):
    k = len(a)
    if k % 2 == 1:
        return a[k // 2]
    return (a[k // 2] + a[k // 2 - 1]) / 2.0


# returns biggest index in the array fulfilling predicate
# O(log(n))
def binary_search(arr, predicate):
    if not arr or not predicate(arr[0]):
        return -1

    def find(left, right):
        assert left <= right

        if right - left <= 1:
            if predicate(arr[right]):
                assert predicate(arr[left])
                return right
            else:
                return left

        m = (left + right) // 2

        if predicate(arr[m]):
            return find(m, right)
        else:
            return find(left, m)

    return find(0, len(arr) - 1)


# counts number of elements less then or equal to specified value in sorted array
def count_le(arr, target):
    # binary search return last index fulfilling predicate, so +1 to count items
    # given 0-based indexing
    return binary_search(arr, lambda x: x <= target) + 1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print('check: %s' % median(sorted(nums1 + nums2)))

        k, n = len(nums1), len(nums2)
        m = (k + n) // 2

        # O(log(k) + log(n)) ~ O(log(n + k))
        def total_le(x):
            return count_le(nums1, x) + count_le(nums2, x)

        # O(log(k) * log(n + k))
        nums1_idx = binary_search(nums1, lambda x: total_le(x) <= m)
        # O(log(n) * log(n + k))
        nums2_idx = binary_search(nums2, lambda x: total_le(x) <= m)

        if (k + n) % 2 == 1:
            # single item
            if nums1_idx == len(nums1) - 1:
                return nums2[nums2_idx + 1]
            elif nums2_idx == len(nums2) - 1:
                return nums1[nums1_idx + 1]
            else:
                # take item with less "total_le" metric
                a = nums1[nums1_idx + 1]
                b = nums2[nums2_idx + 1]
                if total_le(a) < total_le(b):
                    return a
                else:
                    return b
        else:  # avg of two neighbors
            # take biggest from found numbers, then take smallest from the next to get
            # the next in total order and average them
            a = None
            if nums1_idx != -1:
                a = nums1[nums1_idx]
            if nums2_idx != -1 and (a is None or nums2[nums2_idx] > a):
                a = nums2[nums2_idx]

            # now find the next number (smallest) by the total order
            b = None

            if nums1_idx != len(nums1) - 1:
                b = nums1[nums1_idx + 1]
            if nums2_idx != len(nums2) - 1 and (b is None or nums2[nums2_idx + 1] < b):
                b = nums2[nums2_idx + 1]

            # consider case where all numbers are the same, then both indexes will be
            # -1 from both arrays
            if a is None:
                return b

            assert b is not None

            if total_le(a) != m:
                return b

            return (a + b) / 2.0


if __name__ == '__main__':
    x = Solution()
    # print(x.findMedianSortedArrays([1, 2, 3], []))
    # print(x.findMedianSortedArrays([1, 2, 3, 4], []))
    # print(x.findMedianSortedArrays([0, 0], [0]))
    # print(x.findMedianSortedArrays([0, 0], [0, 0]))
    # print(x.findMedianSortedArrays([1, 3], [2]))
    # print(x.findMedianSortedArrays([1], [2, 3]))
    # print(x.findMedianSortedArrays([1, 3], [2, 4]))
    # print(x.findMedianSortedArrays([1, 1], [2, 2]))
    # print(x.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [7, 8, 9]))
    # print(x.findMedianSortedArrays([1, 1, 1, 1, 2, 2, 3, 4], [3, 3, 3, 3, 3, 5, 10, 20]))
    # print(x.findMedianSortedArrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    # print(x.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
    # print(x.findMedianSortedArrays([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
