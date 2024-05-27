from typing import List
import bisect


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

        # so... what we can do to search for the prefix sums which are in a given
        # range AND which are to the left of the current index is the following
        # we can use sorted range of the prefix sums to find indexes range for
        # the prefix sums that are in a given range by number using the binary
        # search, and then we can count ones which are inside of this range AND
        # to the left of the given index using the binary indexed tree where
        # value is "1" for the index which should be in-scope and 0 otherwise;
        # while we are traversing the prefix sums we gradually mark new prefix
        # sums being "in-scope" for the next iteration;

        # we start with nothing being marked as in-scope
        fenwick = [0] * (n + 2)

        def lsb(index):
            return index & -index

        def fenwick_update(index, value):
            """
            Adds a value at a given index.
            """
            index += 1  # support for 0-based indexes
            while index < len(fenwick):
                fenwick[index] += value
                index += lsb(index)

        def fenwick_query(index):
            """
            Computes prefix sum up to the "index" inclusive.
            """
            index += 1  # support for 0-based indexes
            result = 0
            while index > 0:
                result += fenwick[index]
                index -= lsb(index)
            return result

        def fenwick_range_sum(start, end):
            """
            Returns range sum for indexes [start; end] inclusive;
            """
            result = fenwick_query(end)
            if start > 0:
                result -= fenwick_query(start - 1)
            return result

        prefix_sums_sorted = sorted(prefix_sums)

        # IMPORTANT: fenwick tree is tracking which prefix sum elements are
        # "in-scope" meaning marked to be considered at each given step;
        # as we progress on each step we mark new prefix sum as being in-scope;

        count = 0

        for j in range(n):
            ps_j = prefix_sums[j]

            # index of the current prefix sum inside the sorted prefix sum array
            # NOTE: it is okay if there are multiple prefix sums with the same
            # value, we do not really care about which specific index we use
            # between these same values
            idx = bisect.bisect_left(prefix_sums_sorted, ps_j)
            assert prefix_sums_sorted[idx] == ps_j

            # here is the trick: we need to be able to quickly (faster than O(n))
            # count amount of prefix sums to the left of j index which are in a given range
            # (see above why these boundaries are chosen)
            ps_i_lower = ps_j - upper
            ps_i_upper = ps_j - lower

            # handle the case [0; j] by checking if ps_j is within the range
            # in this case range sum is just equal to the prefix sum
            # TODO: can this edge-case be normalized somehow?
            if upper >= ps_j >= lower:
                count += 1

            # now find the indexes
            assert ps_i_lower <= ps_i_upper
            ps_i_lower_idx = bisect.bisect_left(prefix_sums_sorted, ps_i_lower)
            ps_i_upper_idx = bisect.bisect_left(prefix_sums_sorted, ps_i_upper)

            # if we did not find an exact number, then go 1 item back as the index
            # will be inclusively calculated
            if ps_i_upper_idx == n or prefix_sums_sorted[ps_i_upper_idx] != ps_i_upper:
                ps_i_upper_idx -= 1

            count += fenwick_range_sum(ps_i_lower_idx, ps_i_upper_idx)

            # mark current prefix sum as in-scope for further calculations
            fenwick_update(idx, +1)

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.countRangeSum([-2, 5, -1], -2, 2))
