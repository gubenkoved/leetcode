from typing import List
import heapq
import math


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heap = []

        for start, end in points:
            heapq.heappush(heap, (end, start))

        count = 0
        arrow_at = -math.inf

        while heap:
            # send arrow at the end of the first balloon by "end" ascending
            end, start = heapq.heappop(heap)

            if start <= arrow_at:
                # already burst!
                pass
            else:  # send a new arrow!
                count += 1
                arrow_at = end

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(x.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(x.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
