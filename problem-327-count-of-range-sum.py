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

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]

        # calculate all the prefix sums in O(n)
        for idx in range(1, n):
            prefix_sums[idx] = prefix_sums[idx - 1] + nums[idx]

        # the naive solution requires enumerating all the O(n^2) pairs of the
        # prefix sums and this does not pass the time limit

        # however, given the limitation of the lower and upper being from
        # -10^5 to +10^5 we can more efficiently run range queries using
        # segment trees of fenwick tree in the following way:
        # we iterate the prefix sums, and we want to quickly find the amount of
        # prefix sums inside some range;

        # S(i, j) = PS(j) - PS(i - 1)
        # where S(i, j) is range sum from i-th to j-th element inclusive
        #       PS(j) is prefix sum from 0-th to j-th

        # when the j is fixed we fix PS(j), then we need to count amount of prefix
        # sums PS(i) to the left within the following range:
        #
        # lower <= S(i, j) <= upper
        # lower <= PS(j) - PS(i - 1) <= upper
        # lower - PS(j) <= -PS(i - i) <= upper - PS(j)
        # PS(j) - lower >= PS(i - 1) >= PS(j) - upper

        # well... the problem here is that the range is no longer [lower, upper]

        count = 0
        fenwick = [0] * (2 * (10 ** 5))

        def update(index, value):
            pass

        def query(index):
            pass

        for i in range(n):
            pass

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.countRangeSum([-2, 5, -1], -2, 2))
