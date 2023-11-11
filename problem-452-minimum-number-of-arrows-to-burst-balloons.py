from typing import List
import math


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorting by end of interval ascending
        points_sorted = sorted(points, key=lambda interval: interval[1])

        count = 0
        arrow_at = -math.inf

        for start, end in points_sorted:
            # check if already burst!
            if start <= arrow_at:
                continue

            # send a new arrow!
            count += 1
            arrow_at = end

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(x.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(x.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
