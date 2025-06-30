from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, 0
        result = 0
        while l != n - 1:
            while r < n - 1 and nums[r + 1] - nums[l] <= 1:
                r += 1
                # check if harmonious and update the result
                if nums[r] - nums[l] == 1:
                    result = max(result, r - l + 1)
            # move further
            r += 1
            if r == n:
                break
            while l != n - 1 and nums[r] - nums[l] > 1:
                l += 1
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.findLHS([1,3,2,2,5,2,3,7]))
    print(x.findLHS([1, 1, 1, 1]))
