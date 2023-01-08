# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] being True means that first i chars from string matched by
        # first j chars from the pattern
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # assume that empty pattern matches empty string
        dp[0][0] = True

        # fill first row (for empty string) -- we match until we hit first non "*"
        for j in range(len(p)):
            if p[j] != '*':
                break
            dp[0][j + 1] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # we match on wildcard if we previously matched shorter string
                    # then wildcard is expanded to whatever is a new char, or
                    # we matched current string using a pattern w/o wildcard before
                    # then the wildcard is expanded to emptiness
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:  # regular char or "?"
                    if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[len(s)][len(p)]


if __name__ == '__main__':
    import sys
    x = Solution()

    # basic tests
    assert x.isMatch('', '')
    assert not x.isMatch('a', '')
    assert not x.isMatch(' ', 'a')
    assert x.isMatch('aa', 'aa')
    assert not x.isMatch('aab', 'aac')

    assert x.isMatch('ab', 'a*b')
    assert x.isMatch('abab', 'a*b')
    assert x.isMatch('abbbb', 'a*b')
    assert x.isMatch('aaaab', 'a*b')
    assert x.isMatch('acccb', 'a*b')
    assert not x.isMatch('acccba', 'a*b')
    assert not x.isMatch('aba', 'a*b')

    assert x.isMatch('a', 'a*')
    assert x.isMatch('aaaa', 'a*')
    assert x.isMatch('abbb', 'a*')
    assert x.isMatch('abbbccc', 'a*')
    assert not x.isMatch('ba', 'a*')
    assert not x.isMatch('b', 'a*')

    assert x.isMatch('ab', 'a**b')
    assert x.isMatch('aaaabbbb', 'a**b')
    assert not x.isMatch('ac', 'a**b')

    assert x.isMatch('aqb', 'a*?b')
    assert x.isMatch('aqweqb', 'a*?b')
    assert x.isMatch('abqb', 'a*?b')
    assert not x.isMatch('ab', 'a*?b')
    assert not x.isMatch('a', 'a*?b')
    assert not x.isMatch('', 'a*?b')

    assert x.isMatch('aqb', 'a?*b')
    assert x.isMatch('abb', 'a?*b')
    assert x.isMatch('aqcccb', 'a?*b')
    assert not x.isMatch('ab', 'a?*b')
    assert not x.isMatch('a', 'a?*b')

    assert x.isMatch('', '*')
    assert x.isMatch('', '**')
    assert x.isMatch('', '***')
    assert x.isMatch('a', '*')
    assert x.isMatch('a', '**')
    assert x.isMatch('a', '***')
    assert x.isMatch('aaaa', '*')
    assert x.isMatch('aaaa', '**')
    assert x.isMatch('aaaa', '***')

    # user input test
    if len(sys.argv) == 3:
        print(x.isMatch(sys.argv[1], sys.argv[2]))

