from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # each K basically define a separate sub-lanes which can be separately
        # processed in linear time -- this can done via calculating max of the
        # prefix sum inside each lane
        n = len(energy)
        best = float('-inf')
        for lane_idx in range(k):
            cur_best = float('-inf')
            idx = n - lane_idx - 1
            cum_sum = 0
            while idx >= 0:
                val = energy[idx]
                cum_sum += val
                cur_best = max(cur_best, cum_sum)
                idx -= k
            best = max(best, cur_best)
        return best
