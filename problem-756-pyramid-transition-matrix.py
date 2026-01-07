import functools
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        @functools.lru_cache()
        def possible_top(left, right):
            result = set()
            for x in allowed:
                if x[0] == left and x[1] == right:
                    result.add(x[2])
            return result

        # recursive function that returns bool showing if it is possible to
        # construct pyramid with lower level being lower and current level
        # prefix being what specified as well
        def f(lower: str, prefix: str) -> bool:
            # base case
            if len(lower) == 2:
                # check if there is any possible alternative
                return bool(possible_top(lower[0], lower[1]))

            # level is full -> next level
            if len(prefix) == len(lower) - 1:
                return f(prefix, '')

            offset = len(prefix)
            left, right = lower[offset], lower[offset + 1]

            for p in possible_top(left, right):
                if f(lower, prefix + p):
                    return True

            return False

        return f(bottom, '')


if __name__ == '__main__':
    x = Solution()
    print(x.pyramidTransition(bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]))
    print(x.pyramidTransition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]))
