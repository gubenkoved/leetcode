from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        # print('%s, %s' % (s1, s2))

        if s1 == s2:
            return True

        n = len(s1)
        counts = [0] * 26

        for idx in range(n):
            counts[ord(s1[idx]) - ord('a')] += 1
            counts[ord(s2[idx]) - ord('a')] -= 1

        for idx in range(26):
            if counts[idx] != 0:
                return False

        for idx in range(1, n):
            if self.isScramble(s1[:idx], s2[:idx]) and self.isScramble(s1[idx:], s2[idx:]):
                return True

            if self.isScramble(s1[:idx], s2[n-idx:]) and self.isScramble(s1[idx:], s2[:n-idx]):
                return True

        return False


if __name__ == '__main__':
    x = Solution()
    assert x.isScramble('ab', 'ba')
    assert x.isScramble('abc', 'bca')
    assert x.isScramble('great', 'rgeat')
    assert not x.isScramble('abcde', 'caebd')
    assert x.isScramble('abcdbdacbdac', 'bdacabcdbdac')
