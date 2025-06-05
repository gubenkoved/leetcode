from typing import List
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for x in nums if math.floor(math.log10(x)) % 2 == 1)

if __name__ == '__main__':
    x = Solution()
    print(x.findNumbers([100000]))
    print(x.findNumbers([100000 - 1]))
