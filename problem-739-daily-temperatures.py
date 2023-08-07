from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        result = [0] * n

        queue = deque()
        queue.append((temperatures[n - 1], n - 1))

        for idx in range(n - 2, -1, -1):
            while queue and temperatures[idx] >= queue[0][0]:
                queue.popleft()

            if queue:
                _, bigger_idx = queue[0]
                result[idx] = bigger_idx - idx
            else:
                result[idx] = 0

            queue.appendleft((temperatures[idx], idx))

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(x.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
