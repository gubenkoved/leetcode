# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


# see https://research.swtch.com/glob

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0

        restart_idx = None

        while True:
            # either string end or pattern end reached
            s_consumed = s_idx == len(s)
            p_consumed = p_idx == len(p)

            if s_consumed or p_consumed:
                # edge case -- terminating "*" wildcard
                if s_consumed and not p_consumed:
                    # consume all trailing "*" from pattern
                    while p_idx < len(p) and p[p_idx] == '*':
                        p_idx += 1
                        p_consumed = p_idx == len(p)

                matched = s_consumed and p_consumed

                if matched:
                    return True
                elif restart_idx is not None:
                    # print('1. restart using %s' % (restart_idx,))
                    s_idx, p_idx = restart_idx
                    restart_idx = None
                    continue
                else:
                    return False

            p_chr = p[p_idx]
            s_chr = s[s_idx]

            if p_chr == '?' or p_chr == s_chr:
                # advance both pointers
                s_idx += 1
                p_idx += 1
                continue

            elif p_chr == '*':

                # if the expansion won't work out, try again
                # consuming one char from the input
                if s_idx < len(s):
                    restart_idx = (s_idx + 1, p_idx)

                # handle expansion to zero chars
                p_idx += 1
                continue

            if restart_idx is not None:
                # print('2. restart using %s' % (restart_idx,))
                s_idx, p_idx = restart_idx
                restart_idx = None
                continue

            # mismatch
            return False

        raise Exception('not reachable')


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
    print(x.isMatch(sys.argv[1], sys.argv[2]))

