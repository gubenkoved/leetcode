class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        assert len(s1) == len(s2)

        def scramble(s):
            # print('scramble(%s)' % s)

            yield s

            if len(s) == 1:
                return

            for idx in range(1, len(s)):
                left = s[:idx]
                right = s[idx:]

                for a in scramble(left):
                    for b in scramble(right):
                        yield a + b
                        yield b + a

        for x in scramble(s1):
            # print('%s' % x)
            if x == s2:
                return True

        return False


if __name__ == '__main__':
    x = Solution()
    # assert x.isScramble('ab', 'ba')
    # assert x.isScramble('great', 'rgeat')
    # assert not x.isScramble('abcde', 'caebd')
    assert x.isScramble('abcdbdacbdac', 'bdacabcdbdac')
