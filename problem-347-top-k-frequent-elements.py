from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        freq_items = [(freq, key) for key, freq in freq.items()]
        freq_items.sort(reverse=True)

        return [x for _, x in freq_items[:k]]
