from typing import List
from bisect import bisect_left


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pick all pairs and third number is binary search found
        # which gives O(n*n*log(n))
        nums.sort()
        n = len(nums)
        results = set()
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                needed = -1 * (nums[i] + nums[j])
                k = bisect_left(nums, needed, j + 1)
                if k < n and nums[k] == needed:
                    results.add((nums[i], nums[j], nums[k]))
        return [list(x) for x in results]


if __name__ == '__main__':
    x = Solution()
    print(x.threeSum([-1, 0, 1, 2, -1, -4]))
    print(x.threeSum([0, 1, 1]))
    print(x.threeSum([0, 0, 0]))
    print(x.threeSum([1,2,-2,-1]))
