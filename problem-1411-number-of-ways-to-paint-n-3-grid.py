import functools
import sys

sys.setrecursionlimit(10**6)

class Solution:
    def numOfWays(self, n: int) -> int:
        alphabet = ['R', 'Y', 'B']

        def gen(k: int, prev: str) -> list[str]:
            result = []
            for x in alphabet:
                if x == prev:
                    continue
                if k == 1:
                    result.append(x)
                else:
                    for inner in gen(k - 1, x):
                        result.append(x + inner)
            return result

        # gen all triples
        all_possible = gen(3, '')

        M = 10 ** 9 + 7

        def compatible(prev, cur):
            for idx in range(len(prev)):
                if prev[idx] == cur[idx]:
                    return False
            return True

        # count of ways to get to given end result after n steps
        @functools.lru_cache(maxsize=None)
        def f(n, target):
            if n == 1:
                return target in all_possible

            res = 0
            for prev in all_possible:
                if not compatible(prev, target):
                    continue
                res += f(n - 1, prev)
            return res % M

        result = 0
        for target in all_possible:
            result += f(n, target)
        return result % M

if __name__ == "__main__":
    x = Solution()
    print(x.numOfWays(1), 12)
    print(x.numOfWays(5000), 30228214)
