from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        x, y = points[0]
        for idx in range(1, len(points)):
            px, py = points[idx]
            dx, dy = abs(px - x), abs(py - y)
            result += max(dx, dy)
            x, y = px, py
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]), 7)
