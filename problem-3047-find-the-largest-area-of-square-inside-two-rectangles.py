from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        def intersect(r1, r2):
            if r1[0] > r2[0]:
                r1, r2 = r2, r1

            if r2[0] > r1[1]:
                return 0

            return min(r1[1], r2[1]) - min(r1[1], r2[0])

        def calc(i, j):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]

            x1_j, y1_j = bottomLeft[j]
            x2_j, y2_j = topRight[j]

            x_intersection = intersect([x1_i, x2_i], [x1_j, x2_j])
            y_intersection = intersect([y1_i, y2_i], [y1_j, y2_j])

            s = min(x_intersection, y_intersection)
            return s * s


        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                result = max(result, calc(i, j))
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]), 1)
