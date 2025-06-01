from typing import List
from functools import cache


@cache
def dist(w1, w2):
    assert len(w1) == len(w2)
    return sum(1 for c1, c2 in zip(w1, w2) if c1 != c2)


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        # dp[i] is the longest subsequence that ends with i-th word
        dp = [None] * n
        dp[0] = 1
        parent = [None] * n
        dp_best = 1
        dp_best_idx = 0

        for j in range(1, n):
            best = 1
            for i in range(j):
                if len(words[i]) != len(words[j]):
                    continue
                if groups[i] == groups[j]:
                    continue
                if dist(words[i], words[j]) != 1:
                    continue
                if dp[i] + 1 > best:
                    best = dp[i] + 1
                    # remember the index that led to the best result
                    parent[j] = i
            dp[j] = best
            if best > dp_best:
                dp_best = best
                dp_best_idx = j

        # restore the words
        result = []

        ptr = dp_best_idx
        while ptr is not None:
            result.append(words[ptr])
            ptr = parent[ptr]

        return list(reversed(result))


if __name__ == '__main__':
    x = Solution()
    print(x.getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2]))
    print(x.getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4]))
    print(x.getWordsInLongestSubsequence(["za","ay","aa","ba","bb","bc"], [5,4,3,3,2,1]))
