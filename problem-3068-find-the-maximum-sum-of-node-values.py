from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # looks like edges are not needed as toggling allows to reach ANY state
        # with the only constraint: amount of toggled nodes is even
        diffs = [(x ^ k) - x for x in nums]
        diffs.sort(reverse=True)
        best_diff = 0
        idx = 0
        n = len(diffs)
        while idx + 1 < n and diffs[idx] + diffs[idx + 1] > 0:
            best_diff += diffs[idx] + diffs[idx + 1]
            idx += 2
        return sum(nums) + best_diff


if __name__ == '__main__':
    x = Solution()
    assert x.maximumValueSum([1,2,1], 3, [[0,1],[0,2]]) == 6
