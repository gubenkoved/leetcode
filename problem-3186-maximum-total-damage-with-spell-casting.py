from typing import List
from collections import Counter
from functools import cache


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        uniq = list(set(power))
        uniq_n = len(uniq)
        uniq.sort()

        @cache
        def max_damage(start_idx):
            # there are basically two cases -- we either take the element
            # at start idx OR we do not, and we memomize the result

            # base cases
            if start_idx >= uniq_n:
                return 0
            elif start_idx == uniq_n - 1:
                return uniq[start_idx] * counts[uniq[start_idx]]

            # suppose we take number at start idx
            power = uniq[start_idx]
            damage_if_took = power * counts[power]

            # now we just need to find index from which we have spells of
            # allowed powers which are all with value > power + 2
            # (there are only 3 cases really -- +1, +2 or +3 given uniqueness)
            start_idx_if_took = start_idx + 1
            while start_idx_if_took < uniq_n and uniq[start_idx_if_took] <= power + 2:
                start_idx_if_took += 1

            return max(
                damage_if_took + max_damage(start_idx_if_took),
                max_damage(start_idx + 1),
            )

        return max_damage(0)


if __name__ == '__main__':
    x = Solution()
    # print(x.maximumTotalDamage([7,1,6,6]), 13)
    # print(x.maximumTotalDamage([4,5,5,6,3,6,5,3,4]), 18)
    print(x.maximumTotalDamage([3,4,8,10,8,8,3]), 30)