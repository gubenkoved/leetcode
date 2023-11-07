from typing import List
import heapq


# I was trying to solve using just pointers with careful positioning
# using binary search, but could not handle all the edge cases...
# then I've looked up tags for the question, and it mentioned "heap"
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []
        cutoff = None
        max_sum = nums1[0] + nums2[0]

        for num1 in nums1:
            for num2 in nums2:
                s = num1 + num2

                if cutoff is not None and s > cutoff:
                    continue

                heapq.heappush(heap, (s, num1, num2))

                max_sum = max(max_sum, s)

                if len(heap) > k:
                    cutoff = max_sum

        while heap and len(result) < k:
            _, a, b = heapq.heappop(heap)
            result.append([a, b])

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=3))
    # print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=4))
    # print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=6))
    print(x.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=9))
    # print(x.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
    # print(x.kSmallestPairs([1, 2, 4], [-1, 1, 2], k=100))
    # print(x.kSmallestPairs([1, 1, 1], [1, 1, 1], k=20))
    print(x.kSmallestPairs([0, 10, 20, 30, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=51))
