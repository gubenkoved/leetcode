from typing import List
import heapq


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        points = []

        # point types:
        # 0 -- start
        # 1 -- end
        # NOTE: it is important for simplicity of the algorithm below to process
        # starts before the ends, so we need to have "start" metric lower than "end"
        # in our heap

        # not very time efficient but elegant IMO
        for start, end in intervals:
            heapq.heappush(points, (start, 0))
            heapq.heappush(points, (end, 1))

        # add new interval
        heapq.heappush(points, (newInterval[0], 0))
        heapq.heappush(points, (newInterval[1], 1))

        result = []

        depth = 0
        start = None

        while points:
            point, point_type = heapq.heappop(points)

            if point_type == 0:
                if depth == 0:
                    start = point
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    result.append((start, point))

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
