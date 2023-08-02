from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        best_profit = 0
        for idx in range(1, len(prices)):
            best_profit = max(best_profit, prices[idx] - min_so_far)
            min_so_far = min(min_so_far, prices[idx])
        return best_profit
