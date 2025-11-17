from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # each K basically define a separate sub-lanes which can be separately
        # processed in linear time -- this can done via calculating max of the
        # prefix sum inside each lane

        best = float('-inf')
        for lane_idx in range(k):
            lane = energy[lane_idx::k]

            # now process the lane using prefix sums, or rather suffix sums
            cur_best = float('-inf')
            cum_sum = 0
            for val in reversed(lane):
                cum_sum += val
                cur_best = max(cur_best, cum_sum)

            best = max(best, cur_best)

        return best
