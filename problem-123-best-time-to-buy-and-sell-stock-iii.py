from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # a[i] is best profit using single trx from day zero till day "i"
        # b[i] is best profit using single trx from day "i" till day "n"
        # both can be computed in linear time, and then we can get final answer
        # in single pass as well, so overall will be linear
        a = [0] * n
        b = [0] * (n + 1)

        rolling_min = prices[0]
        best_profit = 0
        for day in range(1, n):
            best_profit = max(best_profit, prices[day] - rolling_min)
            rolling_min = min(rolling_min, prices[day])
            a[day] = best_profit

        rolling_max = prices[-1]
        best_profit = 0
        for day in range(n - 2, -1, -1):
            best_profit = max(best_profit, rolling_max - prices[day])
            rolling_max = max(rolling_max, prices[day])
            b[day] = best_profit

        final = 0
        for day in range(1, n):
            final = max(final, a[day] + b[day + 1])

        return final


if __name__ == '__main__':
    x = Solution()
    assert x.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert x.maxProfit([1, 2, 3, 4, 5]) == 4
    assert x.maxProfit([7, 6, 4, 3, 1]) == 0
    assert x.maxProfit(list(range(10000, 0, -1))) == 0
