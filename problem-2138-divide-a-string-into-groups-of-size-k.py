from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for idx in range(0, len(s), k):
            g = s[idx:idx+k]
            if len(g) < k:
                g += fill * (k - len(g))
            result.append(g)
        return result
