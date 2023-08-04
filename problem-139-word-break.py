from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @lru_cache()
        def can_break(cur):
            if cur in words:
                return words

            for idx in range(1, len(cur)):
                left = cur[:idx]

                if left in words:
                    if can_break(cur[idx:]):
                        return True

            return False

        return can_break(s)


if __name__ == '__main__':
    x = Solution()
    print(x.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(x.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
