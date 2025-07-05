from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        freq = Counter(arr)
        for x, f in freq.items():
            if f == x:
                if answer is -1:
                    answer = x
                else:
                    answer = max(answer, x)
        return answer
