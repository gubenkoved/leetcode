from typing import List
import heapq


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        starts_heap = []
        ends_heap = []
        for start, end in queries:
            heapq.heappush(starts_heap, start)
            heapq.heappush(ends_heap, end)

        n = len(nums)
        depth = 0

        for idx in range(n):
            # process all the range openings which are hit
            while starts_heap and starts_heap[0] <= idx:
                depth += 1
                heapq.heappop(starts_heap)

            if nums[idx] > depth:
                return False

            # process ends
            while ends_heap and ends_heap[0] <= idx:
                depth -= 1
                heapq.heappop(ends_heap)

        return True


if __name__ == '__main__':
    x = Solution()
    print(x.isZeroArray(nums = [1,0,1], queries = [[0,2]]))
    print(x.isZeroArray([4,3,2,1], queries = [[1,3],[0,2]]))
