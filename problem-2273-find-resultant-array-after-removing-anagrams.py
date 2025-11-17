from typing import List
from collections import Counter


def letter_counts(word):
    return Counter(word)


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []

        prev_counts = {}
        for word in words:
            counts = letter_counts(word)
            if counts != prev_counts:
                result.append(word)
                prev_counts = counts

        return result
