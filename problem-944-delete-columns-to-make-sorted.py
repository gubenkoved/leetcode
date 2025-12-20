from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col in range(len(strs[0])):
            is_sorted = True
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    is_sorted = False
                    break
            if not is_sorted:
                result += 1
        return result
