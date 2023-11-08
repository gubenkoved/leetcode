from typing import List
import heapq


# I was trying to solve using just pointers with careful positioning
# using binary search, but could not handle all the edge cases...
# then I've looked up tags for the question, and it mentioned "heap"
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []

        # imagine all possible sums as a matrix of size N1 x N2, cells in this
        # matrix will contain the sum;
        # we can start by adding "first row" into the heap, then we will take the
        # one with the smallest sum and replace this element in the heap which is
        # directly "under it";
        # we also store in the heap "row" and "col" that corresponds to the "row"
        # and "column" that sum is attributed to;

        for col, num in enumerate(nums1):
            heapq.heappush(heap, (num + nums2[0], 0, col))

        while len(result) < k and heap:
            # take the smallest element
            s, row, col = heapq.heappop(heap)
            result.append([nums1[col], nums2[row]])

            # add new element to the heap which is directly "under" the one we just
            # removed from the heap
            if row != len(nums2) - 1:
                heapq.heappush(heap, (nums1[col] + nums2[row + 1], row + 1, col))

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=3))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=4))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=6))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=9))
    print(x.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
    print(x.kSmallestPairs([1, 2, 4], [-1, 1, 2], k=100))
    print(x.kSmallestPairs([1, 1, 1], [1, 1, 1], k=20))
    print(x.kSmallestPairs([0, 10, 20, 30, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=51))
