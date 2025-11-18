from typing import List
import bisect


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()

        p = len(potions)
        for spell_power in spells:
            target_potion_strength = success / spell_power
            potion_idx = bisect.bisect_left(potions, target_potion_strength)
            result.append(p - potion_idx)

        return result
