from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # updated value can be calculated using range sums for the original
        # strategy yield and for the prices themselves as updated strategy
        # only uses single range of the "sell" days
        # x x x 0 0 0 0 1 1 1 1 x x x x x   <<<< prev step
        # x x x x 0 0 0 0 1 1 1 1 x x x x   <<<< new step

        n = len(prices)

        orig_strategy_prefix_sums = [0] * (n + 1)
        prices_prefix_sum = [0] * (n + 1)

        for idx in range(n):
            orig_strategy_prefix_sums[idx + 1] = orig_strategy_prefix_sums[idx] + prices[idx] * strategy[idx]
            prices_prefix_sum[idx + 1] = prices_prefix_sum[idx] + prices[idx]

        result = orig_strategy_prefix_sums[n]

        # try to improve the result using updated strategy
        # x x x x 0 0 0 0 1 1 1 1 x x x x   <<<< new step
        #         ^     ^       ^
        #       offset       offset + k - 1
        #          offset + k//2 - 1
        for offset in range(n - k + 1):
            # prefix with original strategy
            cur = orig_strategy_prefix_sums[offset]

            # updated range
            cur += prices_prefix_sum[offset+k] - prices_prefix_sum[offset + k // 2]

            # suffix with original strategy
            cur += orig_strategy_prefix_sums[n] - orig_strategy_prefix_sums[offset + k]

            result = max(result, cur)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2), 10)
