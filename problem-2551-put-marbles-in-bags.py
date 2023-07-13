from typing import List
import heapq


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        if k == n:
            return 0

        max_heap = []
        min_heap = []

        for idx in range(n - 1):
            heapq.heappush(max_heap, -1 * (weights[idx] + weights[idx + 1]))
            heapq.heappush(min_heap, +1 * (weights[idx] + weights[idx + 1]))

        result = 0
        for _ in range(k-1):
            result += -1 * heapq.heappop(max_heap)
            result -= +1 * heapq.heappop(min_heap)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.putMarbles([1, 3, 5, 1], k=2))  # 4 as max 10, min 6
    # print(x.putMarbles([1, 3], k=2))
    # print(x.putMarbles([1, 4, 3, 2, 6, 1, 1, 4, 4, 1, 6], k=2))
    print(x.putMarbles([1, 4, 2, 5, 2], k=3))
