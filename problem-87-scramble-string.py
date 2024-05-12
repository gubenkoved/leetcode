from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # print('%s, %s' % (s1, s2))

        assert len(s1) == len(s2)

        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False

        n = len(s1)

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
