# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # build FSM transform table
        # note that "*" char accept anything but does not change the state
        # as we can consume any amount of chars;
        # such states which correspond to "*" char will be stored separately
        # being simply a marker of the existing states

        # char needed to transition from i-state to next state is
        # transitions[i] char
        transitions = []
        # indexes of the states with wildcards
        wildcard_states = set()

        for c in p:
            if c == '?':
                transitions.append('?')
            elif c == '*':
                wildcard_states.add(len(transitions))
            else:
                transitions.append(c)

        states = {0}

        for c in s:
            new_states = set()
            for state in states:
                if state in wildcard_states:
                    new_states.add(state)

                if state < len(transitions):
                    if transitions[state] == c or transitions[state] == '?':
                        new_states.add(state + 1)

            states = new_states

        accept_state = len(transitions)
        return accept_state in states


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
