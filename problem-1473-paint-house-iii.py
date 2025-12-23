import functools
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        # best cost to paint houses start from idx till the very end
        # so that we end up with exactly K communities given the color
        # of previous house (at idx - 1) being "prev_color"
        # (-1 if not defined for the first home)
        impossible = 1_000_000_000

        @functools.lru_cache(None)
        def f(prev_color, idx, k) -> int:
            # if color is not defined we can use any of the n colors
            # if color is defined we just have to use it
            # print('f(%s, %s, %s)' % (prev_color, idx, k))

            # bound condition
            if idx == m:
                if k == 1:
                    return 0
                return impossible

            if k < 0:
                return impossible

            if houses[idx] == 0:
                # we have to paint it, why don't we try all colors?
                best = impossible
                for color in range(1, len(cost[0]) + 1):
                    new_k = k if color == prev_color or prev_color == -1 else k - 1
                    best = min(best, f(color, idx + 1, new_k) + cost[idx][color - 1])
                return best
            else:  # color is already set
                if houses[idx] == prev_color or prev_color == -1:
                    return f(houses[idx], idx + 1, k)
                else:
                    return f(houses[idx], idx + 1, k - 1)

        ret = f(-1, 0, target)

        if ret == impossible:
            return -1

        return ret


if __name__ == '__main__':
    x = Solution()
    # print(x.minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
    # print(x.minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
    print(x.minCost([2,2,1], [[1,1],[3,4],[4,2]], 3, 2, 2))
