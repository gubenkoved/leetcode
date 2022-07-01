# The median is the middle value in an ordered integer list. If the size of the list
# is even, there is no middle value and the median is the mean of
# the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10-5 of the actual answer will be accepted.

import bisect
import heapq


class MedianFinderV1:

    def __init__(self):
        self.data = []

    # O(n)
    def addNum(self, num: int) -> None:
        bisect.insort_left(self.data, num)

    # O(1)
    def findMedian(self) -> float:
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        return (self.data[n // 2] + self.data[n // 2 - 1]) / 2


# recalled approach after seeing discussion headers
class MedianFinder:
    def __init__(self):
        # values in max heap should be less than values in min heap
        # min from min heap and max from max heap will form a median
        # note that values in max_heap are inverted because Python only has min heap
        self.max_heap = []
        self.min_heap = []

    # O(logn)
    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -(self.max_heap[0]):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, +num)

        # rebalance if needed
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                x = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -x)
            else:
                x = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -x)

    # O(1)
    def findMedian(self) -> float:
        n = len(self.min_heap) + len(self.max_heap)
        if n % 2 == 1:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        else:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
