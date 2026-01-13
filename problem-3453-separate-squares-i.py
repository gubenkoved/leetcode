from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        min_y = squares[0][1]
        max_y = squares[0][1] + squares[0][2]
        total_area = 0
        for x, y, l in squares:
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            total_area += l * l

        def area_below(threshold):
            result = 0
            for x, y, l in squares:
                if threshold <= y:
                    continue
                if threshold >= y + l:
                    result += l * l
                    continue
                ratio = (threshold - y) / l
                result += l *l * ratio
            return result

        # binary search answer
        l, r = min_y, max_y
        while r - l > (10 ** -6):
            m = (l + r) / 2

            if area_below(m) >= total_area / 2:
                r = m
            else:
                l = m

        return l


if __name__ == '__main__':
    x = Solution()
    print(x.separateSquares([[0,0,1],[2,2,1]]), 1)
