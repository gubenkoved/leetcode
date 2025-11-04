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

        left = 0
        right = 0
        inside_window = counts.get(unique[0], 0)
        for idx in range(n):
            # left pointer moves forward if the leftmost element is out of
            # reach, right pointer also moves forward until the next advancement
            # will either be out of array or out of reach; every time we update
            # this window we update inside_window count

            # left pointer handling
            while unique[idx] - unique[left] > k:
                inside_window -= counts[unique[left]]
                left += 1

            while right < n - 1 and unique[right + 1] - unique[idx] <= k:
                # advance right forward
                right += 1
                inside_window += counts[unique[right]]

            reachable[idx] = inside_window

        best = 0

        for idx in range(n):
            best = max(
                best,
                # NOTE: deducting self count from reachable as it includes it inside, but we need
                # to treat it differently since it does not cost anything
                counts.get(unique[idx], 0) + min(numOperations, reachable[idx] - counts.get(unique[idx], 0))
            )

        return best


if __name__ == "__main__":
    x = Solution()
    print(x.maxFrequency([1, 4, 5], 1, 2), 2)
    print(x.maxFrequency([5, 11, 20, 20], 5, 1), 2)
    print(x.maxFrequency([5, 64], 42, 2), 2)
    print(x.maxFrequency([2, 20, 22, 22, 42, 42], 63, 5), 6)
