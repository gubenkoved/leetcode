from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque()
        queue.append((amount, 0))

        visited = set()

        while queue:
            key = queue.popleft()
            leftover, count = key

            if leftover in visited:
                continue

            visited.add(leftover)

            if leftover == 0:
                return count

            for coin in coins:
                if coin <= leftover:
                    queue.append((leftover - coin, count + 1))

        return -1


if __name__ == '__main__':
    x = Solution()
    print(x.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999))

