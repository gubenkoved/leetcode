import time
from typing import List


class Solution:
    def profitableSchemes_bf(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        count = 0
        k = len(group)

        def search(idx, n_left, cur_profit):
            nonlocal count

            # end condition
            if idx == k or n_left == 0:
                if cur_profit >= minProfit:
                    count += 1
                return

            # commit crime
            if n_left >= group[idx]:
                search(idx + 1, n_left - group[idx], cur_profit + profit[idx])

            # do not commit crime branch
            search(idx + 1, n_left, cur_profit)

        start_at = time.time()
        search(0, n, 0)

        result = count % (10 ** 9 + 7)

        print('ANSWER: %s (took %0.3f sec)' % (result, time.time() - start_at))

        return result

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        a = [[[None] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]

        def dp(len, n_, p_):

            if a[len][n_][p_] is not None:
                return a[len][n_][p_]

            if len == 0 or n_ == 0:
                result = 1 if p_ <= 0 else 0
                a[len][n_][p_] = result
                return result

            # do not commit
            result = dp(len - 1, n_, p_)

            # commit
            if n_ >= group[len - 1]:
                result += dp(len - 1, n_ - group[len - 1], max(0, p_ - profit[len - 1]))

            a[len][n_][p_] = result

            return result

        return dp(len(group), n, minProfit) % (10 ** 9 + 7)


if __name__ == '__main__':
    x = Solution()
    assert x.profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]) == 2
    assert x.profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]) == 7
    assert x.profitableSchemes(1, 0, [1], [1]) == 2
    assert x.profitableSchemes(2, 0, [1] * 2, [1] * 2) == 4
    assert x.profitableSchemes(3, 0, [1] * 3, [1] * 3) == 8
    assert x.profitableSchemes(10, 1, [1] * 10, [1] * 10) == 1024 - 1
    assert x.profitableSchemes(10, 0, [1] * 10, [1] * 10) == 1024
    assert x.profitableSchemes(95, 53,
                               [82, 7, 18, 34, 1, 3, 83, 56, 50, 34, 39, 38, 76, 92, 71, 2, 6, 74, 1, 82, 22, 73, 88,
                                98, 6, 71, 6, 26, 100, 75, 57, 88, 43, 16, 22, 89, 7, 9, 78, 97, 22, 87, 34, 81, 74, 56,
                                49, 94, 87, 71, 59, 6, 20, 66, 64, 37, 2, 42, 30, 87, 73, 16, 39, 87, 28, 9, 95, 78, 43,
                                59, 87, 78, 2, 93, 7, 22, 21, 59, 68, 67, 65, 63, 78, 20, 82, 35, 86],
                               [45, 57, 38, 64, 52, 92, 31, 57, 31, 52, 3, 12, 93, 8, 11, 60, 55, 92, 42, 27, 40, 10,
                                77, 53, 8, 34, 87, 39, 8, 35, 28, 70, 32, 97, 88, 54, 82, 54, 54, 10, 78, 23, 82, 52,
                                10, 49, 8, 36, 9, 52, 81, 26, 5, 2, 30, 39, 89, 62, 39, 100, 67, 33, 86, 22, 49, 15, 94,
                                59, 47, 41, 45, 17, 99, 87, 77, 48, 22, 77, 82, 85, 97, 66, 3, 38, 49, 60,
                                66]) == 9883351
    assert x.profitableSchemes(64, 0, [80, 40], [88, 88]) == 2
    assert x.profitableSchemes(1, 1, [1, 1, 1, 1, 2, 2, 1, 2, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 2, 2]) == 4
    assert x.profitableSchemes(100, 0, [1] * 100, [1] * 100) == 976371285
    assert x.profitableSchemes(100, 100, [11] * 100, [11] * 100) == 0
