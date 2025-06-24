from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        dist = [n] * n
        d = n

        # direct pass
        for idx in range(n):
            if nums[idx] == key:
                d = 0
            else:
                d += 1
            dist[idx] = d

        # reverse pass
        d = n
        for idx in range(n - 1, -1, -1):
            if nums[idx] == key:
                d = 0
            else:
                d += 1
            dist[idx] = min(dist[idx], d)

        result = []
        for idx in range(n):
            if dist[idx] <= k:
                result.append(idx)
        return result
