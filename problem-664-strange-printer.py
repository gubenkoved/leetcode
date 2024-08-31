import functools
import math


class Solution:
    def strangePrinter(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, j):
            if i == j:
                return 1

            result = math.inf

            for k in range(i, j):
                result = min(
                    result,
                    dp(i, k) + dp(k + 1, j)
                )

            # this part is not really clear... had to look it up why this -1
            # is needed
            if s[i] == s[j]:
                result -= 1

            return result

        return dp(0, len(s) - 1)


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
