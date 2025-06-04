from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            k = x * 10 + y
            if k not in m:
                m[k] = 0
            m[k] += 1
        return sum(((g * (g - 1)) // 2) for g in m.values() if g != 0)
