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

    def change(self, amount: int, coins: List[int]) -> int:

        # returns count of ways to get exactly "target" amount using coins up to
        # the one with index "coin_idx"
        @lru_cache(maxsize=None)
        def count(target, coin_idx):
            if target == 0:
                return 1

            result = 0

            # suppose we do not use coin at given idx
            if coin_idx > 0:
                # same target required but can not use coin at idx "coin_idx"
                result += count(target, coin_idx - 1)

            # use the coin if we can
            if coins[coin_idx] <= target:
                result += count(target - coins[coin_idx], coin_idx)

            return result

        return count(amount, len(coins) - 1)


if __name__ == '__main__':
    x = Solution()
    print(x.change(5, [1, 2, 5]))
    print(x.change(3, [2]))
    print(x.change(3, [3]))
