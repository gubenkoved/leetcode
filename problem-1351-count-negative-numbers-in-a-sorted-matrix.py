from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            for x in row:
                if x < 0:
                    result += 1
        return result
