import math
from functools import lru_cache


class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(k):
            if k == 0:
                return 0
            if k == 1:
                return 1

            best = math.inf
            for idx in range(1, math.ceil(math.sqrt(k) + 1)):
                if idx * idx > k:
                    break
                best = min(best, 1 + f(k - idx*idx))
            return best

        return f(n)


if __name__ == '__main__':
    x = Solution()
    print(x.numSquares(1))
