from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        n = len(bits)
        last_idx = 0
        while idx < n:
            last_idx = idx
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2
        return last_idx == n - 1
