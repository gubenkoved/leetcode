from typing import List
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # naive O(n^2) solution does not work, so we need a quicker way to
        # count numbers which are to the left of the given one in a given range
        # this can be done by sorting the numbers and using fenwick tree for
        # quick count of the numbers in a given range;
        # counting will be done as follows: while we're traversing the numbers
        # we will be marking the number in fenwick tree
        n = len(nums)
        fenwick = [0] * (n + 1)

        def lsb(index):
            return index & -index

        # NOTE: fenwick API will be 0-based, but internally 0 index should not
        # be used, so we will shift the index
        def fenwick_update(index, val):
            index += 1
            while index < len(fenwick):
                fenwick[index] += val
                index += lsb(index)

        def fenwick_query(index):
            index += 1
            result = 0
            while index > 0:
                result += fenwick[index]
                index -= lsb(index)
            return result

        def fenwick_range_sum(from_incl, to_incl):
            result = fenwick_query(to_incl)
            if from_incl > 0:
                result -= fenwick_query(from_incl - 1)
            return result

        nums_sorted = sorted(nums)
        count = 0

        for num in nums:
            idx = bisect.bisect_left(nums_sorted, num)

            # we need to find numbers to the left which are strictly
            # bigger than 2 * current number
            lower_bound = num * 2
            lower_bound_idx = bisect.bisect_right(nums_sorted, lower_bound)

            if lower_bound_idx != n:
                # when lower bound is to the right of the all numbers, then it
                # means that there are no numbers which are bigger that our
                # lower bound
                count += fenwick_range_sum(lower_bound_idx, n - 1)

            fenwick_update(idx, +1)

        return count


if __name__ == '__main__':
    x = Solution()
    assert x.reversePairs([1, 3, 2, 3, 1]) == 2
    assert x.reversePairs([2, 4, 3, 5, 1]) == 3
    assert x.reversePairs([5, 4, 3, 2, 1]) == 4
