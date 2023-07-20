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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        # take i-th element into the result
        # then on [i+1:] array solve two sum in O(n)/O(n)
        # so total should be O(n^2)
        result = set()
        for i in range(0, n - 2):
            freq = {}
            for tmp in range(i + 1, n):
                if nums[tmp] not in freq:
                    freq[nums[tmp]] = 0
                freq[nums[tmp]] += 1
            for j in range(i + 1, n - 1):
                freq[nums[j]] -= 1
                needed = -1 * (nums[i] + nums[j])
                if freq.get(needed, 0) > 0:
                    result_cur = (nums[i], nums[j], needed)
                    result.add(result_cur)
        return [list(x) for x in result]


if __name__ == '__main__':
    x = Solution()
    print(x.threeSum([-1, 0, 1, 2, -1, -4]))
    print(x.threeSum([0, 1, 1]))
    print(x.threeSum([0, 0, 0]))
    print(x.threeSum([1, 2, -2, -1]))
