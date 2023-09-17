import collections
import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        states_map = collections.defaultdict(set)  # state -> [(via, next_state)]
        state_idx = 0
        wildcard_states = set()

        def add_transition(from_state, via, is_wildcard):
            # create a new state if not wildcard, because with "*" wildcard we can
            # actually spin on the same state
            next_state = from_state + 1

            if is_wildcard:
                wildcard_states.add(next_state)

            states_map[from_state].add((via, next_state))

            # while previs state is wildcard state, add a shortcut corresponding to
            # wildcard resolving to 0 matches
            ptr = from_state
            while ptr in wildcard_states:
                states_map[ptr - 1].add((via, next_state))
                ptr -= 1

            # we can spin however we like here
            if is_wildcard:
                states_map[next_state].add((via, next_state))

            return next_state

        # convert pattern to the state machine
        idx = 0

        while idx < len(p):
            c = p[idx]
            is_wildcard = idx + 1 < len(p) and p[idx + 1] == '*'
            if is_wildcard:
                idx += 1
            state_idx = add_transition(state_idx, c, is_wildcard)
            idx += 1

        final_states = {state_idx}

        # edge cases -- add all trailing wildcard states as final
        ptr = state_idx
        while ptr in wildcard_states:
            final_states.add(ptr - 1)
            ptr -= 1

        # try to feed characters into the state machine
        reachable = {0}
        for c in s:
            next_states = set()
            for state in reachable:
                for via, next_state in states_map.get(state, []):
                    if via == c or via == '.':
                        next_states.add(next_state)
            reachable = next_states

        return any(final_state in reachable for final_state in final_states)

    def isMatch(self, s: str, p: str) -> bool:
        # tokenize the pattern processing wildcard construct
        tokens = []
        idx = 0
        while idx < len(p):
            is_wildcard = idx < len(p) - 1 and p[idx + 1] == '*'
            tokens.append((p[idx], is_wildcard))
            idx += 1 if not is_wildcard else 2

        # checks if first "i" characters match first "j" tokens in pattern
        @functools.lru_cache(maxsize=None)
        def match(i, j):
            if i == 0 and j == 0:
                return True

            if i == 0:  # string is empty
                return all(tokens[jj][1] for jj in range(j))  # match if all left are wildcard tokens

            if j == 0:  # pattern is empty
                return False

            # both "i" and "j" are not 0
            # recursion step
            if tokens[j - 1][1]:  # is wildcard token
                char_match = tokens[j - 1][0] in ['.', s[i - 1]]
                return (
                    char_match and match(i - 1, j) or
                    match(i, j - 1)  # case where we expand wildcard into 0 chars
                )
            else:  # is not wildcard token
                char_match = tokens[j - 1][0] in ['.', s[i - 1]]
                return char_match and match(i - 1, j - 1)

        return match(len(s), len(tokens))


if __name__ == '__main__':
    x = Solution()
    # print(x.isMatch(s="aa", p="a"))
    # print(x.isMatch(s="a", p="a"))
    # print(x.isMatch(s="aa", p="aa"))
    # print(x.isMatch(s="aa", p="a*"))
    # print(x.isMatch(s="ab", p=".*"))
    # print(x.isMatch(s="aaa", p="a*a"))
    # print(x.isMatch(s="aaba", p="ab*a*c*a"))
    # print(x.isMatch(s="aaa", p="aaaa"))
    # print(x.isMatch(s="a", p="ab*"))
    assert x.isMatch(s="a", p="ab*a") is False
