from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hi = []
        low = []

        n = len(profits)
        for idx in range(n):
            if capital[idx] <= w:
                heapq.heappush(low, (-profits[idx], capital[idx]))
            else:
                heapq.heappush(hi, (capital[idx], profits[idx]))

        while k > 0:
            # greedily pick best
            if not low:
                break

            k -= 1

            profit, capital = heapq.heappop(low)

            w += -1 * profit

            # move from hi to low while capital allows
            while hi and hi[0][0] <= w:
                capital2, profit2 = heapq.heappop(hi)
                heapq.heappush(low, (-profit2, capital2))

        return w


if __name__ == '__main__':
    x = Solution()
    # print(x.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
    # print(x.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
    print(x.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 9, 10]))
