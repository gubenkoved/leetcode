# Given a sorted integer array nums and an integer n, add/patch elements to the array
# such that any number in the range [1, n] inclusive can be formed by the sum of some
# elements in the array.
#
# Return the minimum number of patches required.

# > 1 <= nums.length <= 1000
# > 1 <= nums[i] <= 10^4
# > nums is sorted in ascending order.
# > 1 <= n <= 2^31 - 1

from typing import List, Set


def reachable(numbers) -> Set[int]:
    if len(numbers) == 1:
        return set(numbers)
    results = set()
    for x in set(reachable(numbers[:-1])):
        # all the previous combinations are still available
        results.add(x)

        # combinations formed by adding last number to any other reachable combinations
        results.add(x + numbers[-1])

    # combination formed by the last number itself
    results.add(numbers[-1])

    return results


def generate_primes():
    yield 1
    primes = [2]
    cur = 3
    while True:
        is_prime = True
        for prime in primes:
            if cur % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(cur)
            yield cur
        cur += 1


class Solution:
    def minPatches_memoryLimit(self, nums: List[int], n: int) -> int:
        possible = reachable(nums)
        patches = 0
        for x in range(1, n + 1):
            if x not in possible:
                print(f'{x} is not possible')
                patches += 1
                print(f'  added {x} to the set')
                # update all possible combinations
                for possible_num in list(possible):
                    possible.add(possible_num + x)
                possible.add(x)
                print(f'  now possible: {possible}')
        return patches

    def minPatches_v0(self, nums: List[int], n: int) -> int:
        # analytical considerations:
        # as soon as we reach a point where last available number is equal to sum of all the numbers
        # we will have to add N = S+1 number to the list (where S is a sum of previous numbers)
        # because numbers in [1, N-1] are reachable when we add number N we also make
        # numbers in range [N, 2*N - 1] available, and the next not reachable number now 2*N

        # TODO: do not track ALL reachable, just track "max covered number"???
        reachable = set()
        patches = 0
        nums_sum = sum(nums)

        # compose already reachable numbers set
        for num in nums:
            for k in list(reachable):
                reachable.add(num + k)
            reachable.add(num)

        num = 1
        while num <= n:
            if num not in reachable:
                print(f'adding {num} to numbers')
                for k in list(reachable):
                    reachable.add(num + k)
                reachable.add(num)
                # print(f'now reachable: {reachable}')

                patches += 1

                # what we just filled in is the number that is equal to sum of all previous numbers minus one
                # it means that [1, S] numbers were fully filled, and we now add S+1 number, it automatically means
                # that [S+1, S+S+1] numbers are also fully covered (as S+1 serves as an
                # "extension" for the full coverage available already for [1, S])
                # so we can from now on check by multiplying num by 2 until we hit the target
                if nums_sum + 1 == num:
                    print('hit fast track condition!')

                    nums_sum += num

                    while nums_sum < n:
                        num *= 2
                        nums_sum += num
                        print(f'adding {num} to numbers (covered up to {nums_sum})')
                        patches += 1

                    break

                nums_sum += num

            # go to the next number
            num += 1

        return patches

    def minPatches(self, nums: List[int], n: int) -> int:
        covered_up_to = 0
        patches = 0
        current = 1

        nums_iter = iter(nums)
        next_num = next(nums_iter, None)

        while current <= n:
            if next_num is not None and current >= next_num:
                # account for next_num
                covered_up_to += next_num
                next_num = next(nums_iter, None)
                current = covered_up_to + 1
                continue

            # if current is not covered we need a new number and the number is going to be
            # the current number we are checking -- it will provide the biggest "extension"
            if current > covered_up_to:
                covered_up_to += current
                current = covered_up_to + 1  # check from the next
                patches += 1

        return patches


if __name__ == '__main__':
    x = Solution()
    # print(reachable([1, 2, 3, 4, 5]))
    # print(x.minPatches([1, 3], n=6))
    # print(x.minPatches([1, 5, 10], n=20))
    # print(x.minPatches([1, 2, 31, 33], n=2147483647))
    # print(reachable([1, 5, 10, 2, 4]))
    # print(x.minPatches([1, 2, 4, 5, 10], n=1000))
    print(x.minPatches([1,2,16,19,31,35,36,64,64,67,69,71,73,74,76,79,80,91,95,96,97], 8))
    print(x.minPatches([5,6,9,14,15,19,21,23,26,29,29,29,30,36,38,38,41,43,51,51,60,62,69,70,70,73,74,77,85,97,100,106,108,109,113,114,132,139,139,140,144,151,154,157,158,161,165,169,171,176,178,180,191,209,213,214,216,224,225,228,230,232,235,240,241,249,250,251,254,256,259,263,268,274,281,282,283,287,290,290,297,300,303,309,310,317,328,329,329,330,333,346,355,362,364,366,380,383,390,395,400,400,402,409,409,412,413,415,415,416,439,442,444,446,447,448,453,455,463,468,472,479,480,482,483,485,493,493,495,502,505,511,514,515,516,517,518,529,545,550,550,551,558,560,561,564,570,571,572,576,578,580,580,581,584,588,596,597,599,601,602,602,603,603,610,623,625,625,626,626,628,632,636,644,650,658,665,672,675,679,685,690,690,692,693,694,695,695,697,701,701,703,706,706,707,718,719,722,728,728,728,731,731,734,734,734,735,736,741,744,746,748,753,755,760,762,765,765,769,773,775,778,780,781,783,784,788,789,794,798,802,809,810,816,817,818,821,825,826,827,830,832,832,834,837,837,839,841,843,844,846,846,850,851,853,854,869,870,872,883,886,892,892,897,902,903,904,905,908,910,913,919,920,922,922,923,926,929,931,939,941,942,946,946,947,947,960,964,970,970,970,974,974,977,977,980,981,982,992,995], 420428))
