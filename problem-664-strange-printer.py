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

        for k in range(1, len(s)):
            left, right = s[:k], s[k:]
            result = min(
                result,
                self.strangePrinter(left) + self.strangePrinter(right)
            )

        # this part is not really clear... had to look it up why this -1
        # is needed
        if s[0] == s[-1]:
            result -= 1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.strangePrinter('aaabbb'))
    print(x.strangePrinter('aaabbbaaaabbbbaaaa'))
    print(x.strangePrinter('aba'))
    print(x.strangePrinter('t'))
    print(x.strangePrinter('gtg'))
    print(x.strangePrinter('bgtgb'))
    print(x.strangePrinter('tbgtgb'))
    print(x.strangePrinter('tbgtgbt'))
    print(x.strangePrinter('tbgtgbtb'))
    print(x.strangePrinter('baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa'))
    print(x.strangePrinter('dcddbaccadbccddabbcdcdbddbaabcbbdaccacbddcdabdb'))
