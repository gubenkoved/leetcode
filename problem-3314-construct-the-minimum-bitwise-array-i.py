from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            cur = -1
            # minimal increase is when the last bit was initially 0
            # (however this is only applicable for 2)
            # max increase after a | (a+1) operation is when number was all 1
            # like 1111, then OR operation with a+1 will double it + 1
            for a in range(x//2, x):
                if (a | (a + 1)) == x:
                    cur = a
                    break
            ans.append(cur)
        return ans


if __name__ == '__main__':
    x = Solution()
    print(x.minBitwiseArray([2,3,5,7]), [-1,1,4,3])
