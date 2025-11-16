from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, freq in Counter(nums).most_common(2)]
