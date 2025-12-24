from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        n = sum(apple)

        for idx in range(len(capacity)):
            n -= capacity[idx]
            if n <= 0:
                return idx + 1

        return -1