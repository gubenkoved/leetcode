import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for x in range(1, n + 1):
            if n % x == 0:
                factors.append(x)
            if len(factors) == k:
                return factors[-1]
        return -1
