import functools
import math


class Solution:
    @functools.lru_cache(maxsize=None)
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        if len(set(s)) == 1:
            return 1

        result = math.inf

        for l in range(len(s)):
            for r in range(l + 1, len(s) + 1):  # exclusive
                # imagine we type [l, r) range
                c = s[l]
                result = min(
                    result,
                    self.strangePrinter(s[0:l]) +
                    (1 + self.strangePrinter(s[l:r].lstrip(c).rstrip(c))) +
                    self.strangePrinter(s[r:])
                )

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.strangePrinter('aaabbb'))
    print(x.strangePrinter('aba'))
    print(x.strangePrinter('t'))
    print(x.strangePrinter('gtg'))
    print(x.strangePrinter('bgtgb'))
    print(x.strangePrinter('tbgtgb'))
    print(x.strangePrinter('tbgtgbt'))
    print(x.strangePrinter('tbgtgbtb'))
    print(x.strangePrinter('baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa'))
