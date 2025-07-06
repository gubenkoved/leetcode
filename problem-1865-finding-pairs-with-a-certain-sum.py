from typing import List
from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_counts[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_counts[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for x in self.nums1:
            result += self.nums2_counts.get(tot - x, 0)
        return result
