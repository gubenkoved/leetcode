from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]

        for idx in range(1, n):
            prefix_sums[idx] = prefix_sums[idx - 1] + nums[idx]

        count = 0

        for i in range(n):
            for j in range(i, n):
                sum_ = prefix_sums[j]
                if i >= 1:
                    sum_ -= prefix_sums[i - 1]
                if lower <= sum_ <= upper:
                    count += 1

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.countRangeSum([-2, 5, -1], -2, 2))
