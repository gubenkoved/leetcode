from collections import Counter
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        min_val, max_val = min(nums), max(nums)
        counts = Counter(nums)
        unique = list(counts.keys())

        # add phantoms to handle edge cases
        phantoms = set()
        for num in unique:
            if num + k < max_val and num + k not in counts:
                phantoms.add(num + k)

            if num - k > min_val and num - k not in counts:
                phantoms.add(num - k)

        unique.extend(phantoms)
        unique.sort()

        n = len(unique)
        reachable = [0] * n

        # TODO: optimize the calculation to avoid O(n^2)
        for idx in range(n):
            for idx2 in range(n):
                if idx == idx2:
                    continue
                # skip phantoms
                if unique[idx2] not in counts:
                    continue
                if abs(unique[idx] - unique[idx2]) <= k:
                    reachable[idx] += counts[unique[idx2]]

        best = 0

        for idx in range(n):
            cur = counts.get(unique[idx], 0) + min(numOperations, reachable[idx])
            best = max(best, cur)

        return best


if __name__ == "__main__":
    x = Solution()
    print(x.maxFrequency([1, 4, 5], 1, 2))
    print(x.maxFrequency([5, 11, 20, 20], 5, 1))
    print(x.maxFrequency([5, 64], 42, 2))
    print(x.maxFrequency([2, 20, 22, 22, 42, 42], 63, 5))
