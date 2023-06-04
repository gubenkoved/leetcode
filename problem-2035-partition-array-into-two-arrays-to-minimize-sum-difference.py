import collections
import math
import time
from typing import List

STARTED_AT = time.time()
PRINT_ORIG = print


def print(text):
    PRINT_ORIG('[%7.3f] %s' % (time.time() - STARTED_AT, text))


class Solution:
    # TLE
    def minimumDifference_naive(self, nums: List[int]) -> int:
        print('solving for %s...' % nums)

        m = min(nums)
        nums = [x - m for x in nums]

        # try to optimize traversal order...
        nums = sorted(nums)
        nums2 = nums[::2] + nums[1::2]
        nums = nums2

        k = len(nums)
        s = sum(nums)

        ideal = s % 2
        min_difference = math.inf
        counter = 0

        def pick(n, idx, cur_sum):
            nonlocal min_difference
            nonlocal counter

            # print('  %spick(%s, %s, %s)' % ('   ' * (k//2 - n) * 2, n, idx, cur_sum))

            counter += 1

            if n == 0:
                cur_difference = abs(s - 2 * cur_sum)
                if cur_difference < min_difference:
                    print('  found %d' % cur_difference)
                    min_difference = cur_difference
                return

            # cut if no better is possible
            if min_difference == ideal:
                return

            if cur_sum > s // 2:
                return

            for i in range(idx, k):
                # filter out cases where we know there will be not enough numbers
                # even if we take all of the leftover ones to the right
                if n <= k - i:
                    pick(n - 1, i + 1, cur_sum + nums[i])

        pick(k // 2, 0, 0)

        print('checked %d combinations' % counter)

        return min_difference

    def find_combinations(self, nums: List[int], target_differences: List[int]):

        m = min(nums)
        nums = [1 + x - m for x in nums]

        k = len(nums)
        s = sum(nums)

        counter = 0
        call_count = 0
        taken = set()

        results = collections.defaultdict(list)
        best_difference = math.inf

        def search(n, idx, cur_sum):
            nonlocal counter
            nonlocal call_count
            nonlocal best_difference

            call_count += 1

            if n == 0:
                counter += 1

                if counter % 10 ** 6 == 0:
                    print('checked %d' % counter)

                cur_difference = abs(s - 2 * cur_sum)
                if cur_difference in target_differences:
                    print('diff %d: %s' % (cur_difference, ', '.join(['%2d' % x for x in taken])))
                    results[cur_difference].append(list(taken))

                if cur_difference < best_difference:
                    print('best so far is %d: %s' % (cur_difference, ', '.join(['%2d' % x for x in taken])))
                    best_difference = cur_difference
                return

            if cur_sum > s // 2:
                return

            for i in range(idx, k):
                taken.add(i)
                search(n - 1, i + 1, cur_sum + nums[i])
                taken.remove(i)

        search(k // 2, 0, 0)

        print('%d combinations' % counter)
        print('%d invocations' % call_count)
        print(results)

    def minimumDifference(self, nums: List[int]) -> int:
        k, s = len(nums), sum(nums)
        nums1, nums2 = nums[:k//2], nums[k//2:]

        # returns array where i-th element is a collection that shows
        # possible sums i elements from the source array
        def possible_sums(a):
            # NOTE: max amount of combinations in each array where
            # is central binomial C(15, 7) or C(15, 8) which is 6435
            result = [set() for _ in range(len(a) + 1)]

            def search(taken_count, start_at, cur_sum):
                result[taken_count].add(cur_sum)

                if taken_count == len(a):
                    return

                # try to take another item
                for idx in range(start_at, len(a)):
                    search(taken_count + 1, idx + 1, cur_sum + a[idx])

            search(0, 0, 0)

            return result

        left_possible = possible_sums(nums1)
        right_possible = possible_sums(nums2)

        # sort numbers for second subarray to be able to run binary search
        for c in range(len(right_possible)):
            right_possible[c] = sorted(right_possible[c])

        best_diff = math.inf

        # return last idx of the element less than of equal to the target
        def binary_search(a, value):
            def f(left_incl, right_excl):
                if right_excl - left_incl <= 1:
                    return left_incl
                mid = (left_incl + right_excl) // 2
                if a[mid] <= value:
                    return f(mid, right_excl)
                else:
                    return f(left_incl, mid)
            return f(0, len(a))

        # take i from one subarray and leftover from another subarray
        for left_count in range(k // 2 + 1):
            for left_sum in left_possible[left_count]:
                # do not try all items from second subarray -- use binary search
                # to find the best one, closest to ideal sum reminder below
                right_count = k // 2 - left_count
                ideal_right_sum = s // 2 - left_sum
                right_possible_sums = right_possible[right_count]

                # binary search first item less than ideal sum
                right_idx = binary_search(right_possible_sums, ideal_right_sum)

                right_sum = right_possible_sums[right_idx]
                best_diff = min(best_diff, abs(s - 2 * (left_sum + right_sum)))

                # try the next element as well
                if right_idx < len(right_possible_sums) - 1:
                    right_sum = right_possible_sums[right_idx + 1]
                    best_diff = min(best_diff, abs(s - 2 * (left_sum + right_sum)))

        print('BEST %d' % best_diff)

        return best_diff


if __name__ == '__main__':
    x = Solution()

    assert x.minimumDifference([3, 9, 7, 3]) == 2
    assert x.minimumDifference([-36, 36]) == 72
    assert x.minimumDifference([2, -1, 0, 4, -2, -9]) == 0
    assert x.minimumDifference([1, 10]) == 9
    assert x.minimumDifference([4, 4, 4, 10]) == 6
    assert x.minimumDifference([1] * 5 + [10]) == 9
    assert x.minimumDifference([100] * 29 + [200]) == 100
    assert x.minimumDifference(
        [7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283, 5919119,
         3093450, 1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873, 302974, 7656726,
         -2572679, 0, 2121026, -5743797, -8897395, -9699694]) == 1
    assert x.minimumDifference(
        [-7016943, 0, 2205243, -794066, -6795006, 5322408, 9699476, 6544247, 6992622, 7272161, 5469637, 4806999,
         -8562708, -5242263, 9037593, -2746735, 8072395, -1386148, 4745179, 3801334, -4086041, 0, 555427, -9249908,
         5045948, -7943170, 1665466, 9514306, 7960606, -142676]) == 1

    # performance test
    for _ in range(10):
        assert x.minimumDifference(
            [-9812803, -9143114, -2074989, -5685138, -7352242, 3440344, -2609145, -8086215, -8560628, 1649530, 9514043,
             -6703707, 2999701, 4558830, -92232, -7002104, -563926, 5824475, 9273165, -5659380, -985282, 5974935, 5385506,
             9920972, 1291494, -3581309, -4123458, -1468372, 2224246, 7135705],
        ) == 2
