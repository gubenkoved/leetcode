from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(maxsize=None)
        def f(i, j, t):
            # print('f(%s, %s, %s)' % (i, j, t))
            # base cases
            if t == 0:
                return 0
            if j - i <= 0:
                return 0

            rolling_min = prices[i]
            best = 0
            for idx in range(i + 1, j + 1):
                if prices[idx] <= rolling_min:
                    rolling_min = min(rolling_min, prices[idx])
                    continue

                # try to sell at this day
                # print('selling at %s with profit %s' % (idx, prices[idx] - rolling_min))
                best = max(
                    best,
                    prices[idx] - rolling_min + f(idx + 1, j, t - 1))
            return best

        return f(0, len(prices) - 1, k)


if __name__ == '__main__':
    x = Solution()
    print(x.maxProfit(k=2, prices=[2, 4, 1]))
    print(x.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
