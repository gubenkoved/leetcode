from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []

        digits_count = Counter(digits)
        for x in range(100, 1000, 2):
            d1 = x % 10
            d2 = (x // 10) % 10
            d3 = (x // 100) % 10

            needed_counts = Counter([d1, d2, d3])
            ok = True
            for d, c in needed_counts.items():
                if digits_count.get(d, 0) < c:
                    ok = False

            if ok:
                result.append(x)

        return result
