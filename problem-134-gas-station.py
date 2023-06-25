from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        cur_balance = gas[0] - cost[0]
        min_balance_idx = 0
        min_balance = cur_balance

        for idx in range(1, n):
            cur_balance += gas[idx] - cost[idx]

            if cur_balance <= min_balance:
                min_balance_idx = idx
                min_balance = cur_balance

        if cur_balance < 0:
            return -1

        return (min_balance_idx + 1) % n


if __name__ == '__main__':
    x = Solution()
    assert x.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert x.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
