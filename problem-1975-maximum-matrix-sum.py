from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs = 0
        negative_count = 0
        zeros_count = 0
        smallest_abs = None
        for row in matrix:
            for x in row:
                total_abs += abs(x)

                if x == 0:
                    zeros_count += 1
                elif x < 0:
                    negative_count += 1

                if smallest_abs is None or abs(x) < smallest_abs:
                    smallest_abs = abs(x)

        if negative_count % 2 == 0 or zeros_count > 0:
            return total_abs

        return total_abs - smallest_abs * 2


if __name__ == '__main__':
    x = Solution()
    print(x.maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]]), 34)
