from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(
            sum(1 for x in row if x < 0)
            for row in grid
        )
