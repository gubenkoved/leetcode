from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        q = min(nums) - k
        for idx in range(len(nums)):
            if nums[idx] - q > k:
                q = nums[idx] - k

            # try to greedily replace if possible
            if abs(nums[idx] - q) <= k:
                nums[idx] = q
                q += 1

        return len(set(nums))


if __name__ == '__main__':
    x = Solution()
    # print(x.maxDistinctElements([7,10,10], 2), 3)
    print(x.maxDistinctElements([9,10,9,9,9], 1), 4)
