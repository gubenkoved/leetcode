import functools
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @functools.lru_cache(maxsize=None)
        def max_profit(from_day, to_day, trx_count) -> int:
            if to_day - from_day < 1:
                return 0

            if trx_count == 1:
                min_price_so_far = prices[from_day]
                result = 0
                for day in range(from_day + 1, to_day + 1):
                    potential_profit = prices[day] - min_price_so_far
                    result = max(result, potential_profit)
                    min_price_so_far = min(min_price_so_far, prices[day])
                return result

            # recursive dive!
            result = 0
            for day in range(from_day, to_day):
                cur_result = max_profit(from_day=from_day, to_day=day, trx_count=trx_count - 1)
                cur_result += max_profit(from_day=day + 1, to_day=to_day, trx_count=1)
                result = max(result, cur_result)

            return result

        return max(
            max_profit(from_day=0, to_day=n - 1, trx_count=2),
            max_profit(from_day=0, to_day=n - 1, trx_count=1)
        )


if __name__ == '__main__':
    x = Solution()
    assert x.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert x.maxProfit([1, 2, 3, 4, 5]) == 4
    assert x.maxProfit([7, 6, 4, 3, 1]) == 0
    assert x.maxProfit(list(range(10000, 0, -1))) == 0
