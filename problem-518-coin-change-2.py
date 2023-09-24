from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1

        coins = sorted(coins)

        @lru_cache(maxsize=None)
        def count(target, min_coin):
            result = 0
            for coin in coins:
                if coin < min_coin:
                    continue
                if coin == target:
                    result += 1
                elif coin < target:
                    result += count(target - coin, coin)
            return result

        return count(amount, coins[0])


if __name__ == '__main__':
    x = Solution()
    print(x.change(5, [1, 2, 5]))
    print(x.change(3, [2]))
    print(x.change(3, [3]))
