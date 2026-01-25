from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            cur = -1
            for a in range(x):
                if (a | (a + 1)) == x:
                    cur = a
                    break
            ans.append(cur)
        return ans


if __name__ == '__main__':
    x = Solution()
    print(x.minBitwiseArray([2,3,5,7]), [-1,1,4,3])
