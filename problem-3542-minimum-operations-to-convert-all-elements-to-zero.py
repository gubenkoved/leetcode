from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        s = []
        result = 0

        for x in nums:
            while s and x < s[-1]:
                result += 1
                s.pop(-1)

            # do not add a duplicate
            if x != 0 and (not s or s[-1] != x):
                s.append(x)

        return result + len(s)


if __name__ == '__main__':
    x = Solution()
    print(x.minOperations([0,2]), 1)
