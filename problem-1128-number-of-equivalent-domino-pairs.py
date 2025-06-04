from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            k = (x, y)
            if k not in m:
                m[k] = 0
            m[k] += 1
        result = 0
        for g in m.values():
            if g == 0:
                continue
            result += (g * (g - 1)) // 2
        return result
