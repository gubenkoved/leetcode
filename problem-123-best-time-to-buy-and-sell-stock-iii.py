from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        cache = {}

        def max_profit(to_day, trx_count) -> int:
            cache_key = (to_day, trx_count)
            if cache_key in cache:
                return cache[cache_key]

            if to_day < 1:
                return 0

            if trx_count == 1:
                min_price_so_far = prices[0]
                result = 0
                for day in range(to_day + 1):
                    potential_profit = prices[day] - min_price_so_far
                    result = max(result, potential_profit)
                    min_price_so_far = min(min_price_so_far, prices[day])
                cache[cache_key] = result
                return result

            # recursive dive!
            result = 0
            for middle_day in range(to_day - 1):
                cur_result = max_profit(to_day=middle_day, trx_count=trx_count - 1)

                # now we have time from "day" for the last transaction
                min_price_so_far = prices[middle_day + 1]
                best_final_sell = 0
                for final_sell_day in range(middle_day + 2, to_day + 1):
                    potential_profit = prices[final_sell_day] - min_price_so_far
                    best_final_sell = max(best_final_sell, potential_profit)
                    min_price_so_far = min(min_price_so_far, prices[final_sell_day])

                cur_result += best_final_sell
                result = max(result, cur_result)

            cache[cache_key] = result
            return result

        return max(
            max_profit(to_day=n - 1, trx_count=1),
            max_profit(to_day=n - 1, trx_count=2),
        )


if __name__ == '__main__':
    x = Solution()
    assert x.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert x.maxProfit([1, 2, 3, 4, 5]) == 4
    assert x.maxProfit([7, 6, 4, 3, 1]) == 0
    assert x.maxProfit(list(range(10000, 0, -1))) == 0
