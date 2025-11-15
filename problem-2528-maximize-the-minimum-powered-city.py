from typing import List


def is_possible_to_reach(power: List[int], r: int, k: int, target_power: int) -> bool:
    # when we will place a station or multiple stations we need to remember when it goes
    # out of range, this diff will maintain the adjustment needed at a given index;
    # when we have power deficiency at some index i, we will place required number
    # of stations at index i + r, to maximize the benefit for other indexes
    n = len(power)
    diff = [0] * n
    delta_in_range = 0

    for idx in range(n):
        # handle out of range
        delta_in_range += diff[idx]

        effective_power = power[idx] + delta_in_range
        deficiency = target_power - effective_power
        if deficiency > 0:
            # need to place stations here
            if k < deficiency:
                return False

            delta_in_range += deficiency
            k -= deficiency

            # remember when it goes out of range
            if idx + 2 * r + 1 < n:
                diff[idx + 2 * r + 1] -= deficiency

    return True


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        tmp = 0
        left = [0] * n  # left half window sums (excl center)
        for idx in range(1, n):
            tmp += stations[idx - 1]
            if idx - r - 1 >= 0:
                tmp -= stations[idx - r - 1]
            left[idx] = tmp

        tmp = 0
        right = [0] * n  # right half window
        for idx in range(n - 2, -1, -1):
            tmp += stations[idx + 1]
            if idx + r + 1 < n:
                tmp -= stations[idx + r + 1]
            right[idx] = tmp

        # current pow
        power = [0] * n
        for idx in range(n):
            power[idx] = stations[idx] + left[idx] + right[idx]

        # now binary search the answer which is simpler than solve optimally
        # as we can act in a greedy fashion -- ALL the deficiency has to be
        # covered, so we can linearly check if we have enough stations

        min_power = min(power)

        ans_min_incl = min_power  # worst case -- all the stations require lifting
        ans_max_excl = min_power + k + 1  # in the best case we only have this 1 idx that requires lifting

        while ans_max_excl - ans_min_incl > 1:
            ans_check = (ans_min_incl + ans_max_excl) // 2

            if is_possible_to_reach(power, r, k, ans_check):
                ans_min_incl = ans_check
            else:
                ans_max_excl = ans_check

        return ans_min_incl


if __name__ == '__main__':
    x = Solution()
    # 1 2 4 5 0
    # (left sliding window of size 1)
    # 0 1 2 4 5
    # (right)
    # 2 4 5 0 0
    # (total with itself)
    # 3 7 11 9 5
    # print(x.maxPower(stations = [1,2,4,5,0], r = 1, k = 2), 5)
    print(x.maxPower([4, 2], 1, 1), 7)
